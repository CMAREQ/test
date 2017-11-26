import unittest
from scrape import current_target_url, get_total_records, crawler

class TestScrape(unittest.TestCase):

    def setUp(self):
        self.target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
        self.target_url += '?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500'
        self.target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
        self.target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
        self.target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'


    def test_TargetURL(self):
        self.assertEqual(current_target_url(1,0), self.target_url)

    def test_TotalRecords(self):
        self.assertEqual(get_total_records(self.target_url), 4382)

    def test_Crawler(self):
        self.assertTrue(crawler())

    #def test_GetJsonData(self):
    #    self.assertEqual(get_json_data(self.target_url),  {'iTotalRecords': 4382, 'iTotalDisplayRec[80232 chars]>'})

if __name__ == '__main__':
    unittest.main()
