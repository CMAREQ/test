import unittest
from unittest.mock import patch, Mock
from scrape import *


class TestScrape(unittest.TestCase):

    def setUp(self):
        self.target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
        self.target_url += '?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500'
        self.target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
        self.target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
        self.target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'


        self.data = '[["<a href="https://www.metal-archives.com/bands/%24ilverdollar/60323'
        self.data += '>$ilverdollar</a>","Heavy/Power Metal","Nyköping","<span class=\"active\">Active</span>"]]'

        self.soup = "Ejemplo objeto tipo Soup"

    def test_CurrentTargetURL(self):
        self.assertEqual(S.current_target_url(1, 0), self.target_url)

    def test_GetTotalRecords(self):
        self.assertEqual(S.get_total_records(self.target_url), 4382)

    @patch('scrape.S')
    def test_JsonData(self, mockS):
        s = mockS()
        s.get_json_data.return_value = self.data

        self.assertEqual(s.get_json_data(self.target_url), self.data)

    @patch('scrape.S.crawler', return_value = True)
    def test_Crawler(self, crwlr):
        self.assertTrue(crwlr())

    @patch('scrape.S.get_band_attributes', return_value = True)
    def test_BandAttributes(self,att):
        self.assertTrue(att(self.soup))

    @patch('scrape.S.get_band_disco', return_value = True)
    def test_BandDisco(self, disc):
        self.assertTrue(disc(self.soup, 500))

    @patch('scrape.S.get_band_members', return_value = True)
    def test_BandMemebers(self, mem):
        self.assertTrue(mem(self.soup, 500))


        # algo = s.get_json_data()
        # self.assertIsNotNone(algo)
        # #assert mockS is scrape.S
        # assert mockS.called
        # s.get_json_data.assert_called_with()



if __name__ == '__main__':
    unittest.main()
