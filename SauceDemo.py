import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class Saucetest(unittest.TestCase):  

    def setUp(self):
        s = ChromeService(executable_path='chromedriver')
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.saucedemo.com/') 
    

    def test_new_sale(self):
        driver = self.driver
        user_name = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        

        self.assertTrue(user_name.is_enabled()
        and password.is_enabled())
        
        user_name.send_keys('standard_user')
        password.send_keys('secret_sauce')
    
        driver.find_element(By.ID,'login-button').click()
        sleep(3)


        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
        driver.find_element(By.ID,'checkout').click()

        first_name = driver.find_element(By.ID,'first-name')
        last_name = driver.find_element(By.ID,'last-name')
        zip_code = driver.find_element(By.ID,'postal-code')

        self.assertTrue (first_name.is_enabled() and last_name.is_enabled() and zip_code.is_enabled())
        
        first_name.send_keys("Manuel")
        last_name.send_keys("Ledezma")
        zip_code.send_keys("4016")
        driver.find_element(By.ID,'continue').click()
        driver.find_element(By.ID,"finish").click()
        sleep(3)

    def tearDown(self):
        self.driver.close() 


if __name__=='__main__':
    unittest.main (verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name='Purchasesaucedemo'))