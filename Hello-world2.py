import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class helloworld2(unittest.TestCase):
                    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path ="./chromedriver")


    def test_Hello_world_argentina_turismo(self):
        self.driver.get("https://www.argentina.tur.ar")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_Hello_world_sprach(self):
        self.driver.get("https://www.sprachcaffe.com/sa/espanol/main.htm")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_Hello_world_assistcard(self):
        self.driver.get("https://www.assistcard.com/")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)


    def tearDown(self): 
        self.driver.close()

if __name__=="__main__":
    unittest.main (verbosity=2, testRunner = HTMLTestRunner(output="reportes" ,report_name="hello_world_practice2"))
