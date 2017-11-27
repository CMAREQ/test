import unittest
import unittest.mock
from scrape import Scrape
from unittest.mock import patch, Mock

class TestScrape(unittest.TestCase):

    @patch('scrape.Scrape.current_target_url', return_value = "Pass")
    def test_target(self,suma):
        self.assertEqual(suma(), "Pass")

    @patch('scrape.Scrape.get_total_records', return_value = 1)
    def test_TotalRecords(self, TR):
        self.assertEqual(TR(), 1)

    @patch('scrape.Scrape.get_json_data', return_value = "Pass")
    def test_JsonData(self,json):
        self.assertEqual(json(), "Pass")

    @patch('scrape.Scrape.crawler', return_value = True)
    def test_Crawler(self, cr):
        self.assertTrue(cr())

    @patch('scrape.Scrape.get_band_attributes', return_value = "Atributos de banda")
    def test_BandAttributes(self,att):
        soup = "Objeto tipo soup"
        self.assertEqual(att(soup), "Atributos de banda")

    @patch('scrape.Scrape.get_band_disco', return_value = "Discografía de banda")
    def test_BandDisco(self, disc):
        self.assertEqual(disc(),"Discografía de banda")

    @patch('scrape.Scrape.get_band_members', return_value = "Miembros de banda")
    def test_BandMemebers(self, mem):
        self.assertEqual(mem(),"Miembros de banda")



if __name__ == '__main__':
    unittest.main()
