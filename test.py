import unittest
from unittest.mock import patch, Mock
from scrape import *
from crud import *
class TestScrape(unittest.TestCase):

    def setUp(self):
        self.target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
        self.target_url += '?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500'
        self.target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
        self.target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
        self.target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'

        self.data = '[["<a href="https://www.metal-archives.com/bands/Abomation/2853'
        self.data += '>Abomation</a>","Trash Metal","Grängesberg","<span class=\"split-up\">Split-up</span>"]]'



    def test_Factory(self):
        self.assertIsInstance(fact.factory("band"), Band)
        self.assertIsInstance(fact.factory("discography"), Discography)
        self.assertIsInstance(fact.factory("member"), Member)

    def test_CurrentTargetURL(self):
        self.assertEqual(S.current_target_url(1, 0), self.target_url)

    def test_GetTotalRecords(self):
        self.assertEqual(S.get_total_records(self.target_url), 4383)

    def test_Crawler(self):
        self.assertIsNone(S.crawler())

    @patch('crud.print', return_value = " ")
    def test_Select(self, s):
        self.assertIsNone(selectFromBand("- - -"))
        self.assertIsNone(selectFromBand(""))

        self.assertIsNone(selectFromDiscography("- - -"))
        self.assertIsNone(selectFromDiscography(""))

        self.assertIsNone(selectFromMember("- - -"))
        self.assertIsNone(selectFromMember(""))

    def test_Delete(self):
        self.assertIsNone(deleteFromMember("(Jhator)"))
        self.assertIsNone(deleteFromDiscography("(Jhator)"))
        self.assertIsNone(deleteFromBand("(Jhator)"))

    def test_Update(self):
        self.assertIsNone(updateMemberName("Ola Berg", "Adio Berg"))
        self.assertIsNone(updateDiscographyName("Morte", "Moride"))
        self.assertIsNone(updateBandName("- - -", "+ + +"))

if __name__ == '__main__':
    unittest.main()
