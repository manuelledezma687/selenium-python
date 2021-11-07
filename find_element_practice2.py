from typing import Text
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class testheropkuapp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.maximize_window()

    def test_demo(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a').click()
        driver.back()
        driver.find_element_by_partial_link_text("Frames").click()
        driver.implicitly_wait(10)


    def test_demo2(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("A/B Testing").click()
        driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.close()

if __name__ =="__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="reportes", report_name ='test_herokuapp'))