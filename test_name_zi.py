import unittest
from selenium import webdriver
class Test_name(unittest.TestCase):
    def setUp(self):
        self.name = webdriver.Firefox()
    def tearDown(self):
        self.name.quit()
    def test_name_indux(self):
        self.name.get('http://127.0.0.1:8000')
        self.assertIn('worked',self.name.title)
        self.fail('hahaha')
if __name__ == '__main__':
    unittest.main()