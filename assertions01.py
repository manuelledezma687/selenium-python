import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class test_assertion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://blazedemo.com/')

    def test_assertions_one(self):
        self.assertTrue(self.is_element_present(By.NAME,'fromPort'))

    def test_assertions_two(self):
        self.assertTrue(self.is_element_present(By.NAME,'toPort'))
        sleep(4)

    def tearnDown(self):
        self.driver.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__=="__main__":
    unittest.main(verbosity=2, )