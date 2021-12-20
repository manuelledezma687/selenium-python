from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from time import sleep


class nuevotest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('https://www.blazedemo.com/')

    def testprobando(self):
        driver = self.driver
        driver.find_element(By.NAME,"fromPort").send_keys("Boston")
        sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__=="__main__":
    unittest.main(verbosity=2)

