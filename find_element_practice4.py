import unittest
from selenium import webdriver
from time import sleep

class testdemo4 (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def test_demo1(self):
        self.driver.get('http://the-internet.herokuapp.com/')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_partial_link_text('A/B Testing').click()
        driver.back()
        sleep(5)

    def tearnDown(self):
        self.driver.close()


if __name__=="__main__":
    unittest.main(verbosity=2,)