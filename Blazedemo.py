import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep

class NuevoTestPage(unittest.TestCase):  

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://blazedemo.com/') 
    

    def test_new_sale(self):
        driver =self.driver
        driver.find_element_by_xpath("/html/body/div[3]/form/select[1]/option[1]").click()
        driver.find_element_by_xpath("/html/body/div[3]/form/select[2]/option[1]").click()
        driver.find_element_by_css_selector('body > div.container > form > div > input').click()

        driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[1]/input').click()
        driver.find_element_by_xpath("/html/body/div[2]/h2")
        sleep(3)

        first_name = driver.find_element_by_id('inputName')
        address = driver.find_element_by_id('address')
        city = driver.find_element_by_id('city')
        state = driver.find_element_by_id('state')
        zip_code = driver.find_element_by_id('zipCode')
        Card_type = driver.find_element_by_id('cardType')
        credit_card_number = driver.find_element_by_id('creditCardNumber')
        Month = driver.find_element_by_id('creditCardMonth')
        Year = driver.find_element_by_id('creditCardYear')
        name_on_card = driver.find_element_by_id('nameOnCard')
        submit_button = driver.find_element_by_xpath('/html/body/div[2]/form/div[11]/div/input')

        self.assertTrue(first_name.is_enabled()
        and address.is_enabled()
        and city.is_enabled()
        and state.is_enabled()
        and zip_code.is_enabled()
        and Card_type.is_enabled()
        and credit_card_number.is_enabled()
        and Month.is_enabled()
        and Year.is_enabled()
        and name_on_card.is_enabled()
        and submit_button.is_enabled())

        
        first_name.send_keys("Manuel")
        address.send_keys("ABC 1435")
        city.send_keys("MonteCarlo")
        state.send_keys("MonteCarlo")
        zip_code.send_keys("12578")
        Card_type.send_keys("Visa")
        credit_card_number.send_keys("5447895654785214")
        Month.send_keys("11")
        Year.send_keys("2030")
        name_on_card.send_keys("Manuel Ledezma")
        submit_button.click() 
        sleep (3)
        final = driver.find_element_by_tag_name('h1')
        assert final.text == "Thank you for your purchase today!"

    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.close() 


if __name__=='__main__':
    unittest.main (verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name='PurchaseBlazedemo21'))





