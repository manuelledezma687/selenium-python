import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class testphptravels (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = self.driver
        driver.get("https://phptravels.com/demo/")
        driver.maximize_window()

    def test_phptravel(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Pricing").click()

    def test_phptravel2(self):
        driver = self.driver
        driver.find_element_by_css_selector("body > header > div > nav > a:nth-child(2)").click()

    def test_phptravel3(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Mobile Apps").click()
    
    
    def tearDown(self):
        self.driver.close()

if __name__ =="__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="reportes", report_name ='test_phptravels'))