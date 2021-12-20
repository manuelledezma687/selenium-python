import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep

class Saucetest(unittest.TestCase):  

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.saucedemo.com/') 
    

    def test_new_sale(self):
        driver = self.driver
        user_name = driver.find_element_by_id("user-name")
        password = driver.find_element_by_id("password")
        

        self.assertTrue(user_name.is_enabled()
        and password.is_enabled())
        
        user_name.send_keys('standard_user')
        password.send_keys('secret_sauce')
    
        driver.find_element_by_id('login-button').click()
        sleep(3)


        driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
        driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
        driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
        driver.find_element_by_id('checkout').click()

        first_name = driver.find_element_by_id('first-name')
        last_name = driver.find_element_by_id('last-name')
        zip_code = driver.find_element_by_id('postal-code')

        self.assertTrue (first_name.is_enabled() and last_name.is_enabled() and zip_code.is_enabled())
        
        first_name.send_keys("Manuel")
        last_name.send_keys("Ledezma")
        zip_code.send_keys("4016")
        driver.find_element_by_id('continue').click()
        driver.find_element_by_id("finish").click()
        sleep(3)
        

    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.close() 


if __name__=='__main__':
    unittest.main (verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name='Purchasesaucedemo'))