import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class test_helloworld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  ="./chromedriver")


    def test_hello_world_google(self):
        self.driver.get("https://www.google.com/")
        driver = self.driver
        driver.maximize_window()

    def test_hello_world_bing(self):
        self.driver.get("https://www.bing.com/?toWww=1&redig=850D406441AE4277AEED74AE744D8134")
        driver = self.driver
        driver.maximize_window()

    def test_hello_world_platzi(self):
        self.driver.get("https://www.platzi.com/")
        driver = self.driver
        driver.maximize_window()


    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2,testRunner = HTMLTestRunner(output = 'reportes', report_name='helloword-practice1'))