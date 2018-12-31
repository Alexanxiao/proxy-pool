import unittest
from core.crawler import Crawler

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler()

    def test_xici(self):
        res = self.crawler.xici()
        print(res)
        self.assertTrue(len(res)!=0)

    def test_kuaidaili(self):
        res = self.crawler.kuaidaili()
        print(res)
        self.assertTrue(len(res)!=0)

    def test_ip3366(self):
        res = self.crawler.ip3366()
        print(res)
        self.assertTrue(len(res) != 0)

    def test_jiangxianli(self):
        res = self.crawler.jiangxianli()
        print(res)
        self.assertTrue(len(res) != 0)



if __name__ == '__main__':
    unittest.main()