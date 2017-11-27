import unittest
from unittest.mock import patch, Mock
from scrape import current_target_url, get_total_records

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
        self.target_url += '?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500'
        self.target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
        self.target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
        self.target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'

        self.soup = "Ejemplo objeto tipo Soup"

    def test_CurrentTargetURL(self):
        self.assertEqual(current_target_url(1, 0), self.target_url)

    def test_GetTotalRecords(self):
        self.assertEqual(get_total_records(self.target_url), 4382)

    @patch('scrape.get_json_data', return_value = "Data")
    def test_JsonData(self,json):
        self.assertEqual(json(self.target_url), "Data")

    @patch('scrape.crawler', return_value = True)
    def test_Crawler(self, crwlr):
        self.assertTrue(crwlr())

    @patch('scrape.get_band_attributes', return_value = True)
    def test_BandAttributes(self,att):
        self.assertTrue(att(self.soup))

    @patch('scrape.get_band_disco', return_value = True)
    def test_BandDisco(self, disc):
        self.assertTrue(disc(self.soup, 500))

    @patch('scrape.get_band_members', return_value = True)
    def test_BandMemebers(self, mem):
        self.assertTrue(mem(self.soup, 500))



if __name__ == '__main__':
    unittest.main()
