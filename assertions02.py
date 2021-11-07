import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class demosauce (unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path='chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")


    def testsauceone(self):
        self.driver.find_element_by_id('user-name')
        self.assertTrue(self.is_element_present(By.ID, "user-name"))
        self.driver.find_element_by_id('password')
        self.assertTrue(self.is_element_present(By.ID, "password"))
        sleep(5)

    def testsaucedemotwo(self):
        self.assertTrue(self.is_element_present(By.NAME,"login-button"))
        self.assertTrue(self.is_element_present(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]"))
        self.driver.refresh()


    def tearDown(self):
        self.driver.close()

    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by= how, value = what)
        except NoSuchElementException as variable:
            return False
        return True 

if __name__=="__main__":
    unittest.main(verbosity=2,)
