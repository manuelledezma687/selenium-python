import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class NuevoTestPage(unittest.TestCase):  

    def setUp(self):
        s = ChromeService(executable_path = "./chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://blazedemo.com/') 

    def test_new_sale(self):
        driver =self.driver
        driver.find_element(By.XPATH, "/html/body/div[3]/form/select[1]/option[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[3]/form/select[2]/option[1]").click()
        driver.find_element(By.CSS_SELECTOR, 'body > div.container > form > div > input').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[1]/td[1]/input').click()
        driver.find_element(By.XPATH, "/html/body/div[2]/h2")

        driver.find_element(By.ID,'inputName').send_keys("Manuel")
        driver.find_element(By.ID,'address').send_keys("ABC 1435")
        driver.find_element(By.ID,'city').send_keys("MonteCarlo")
        driver.find_element(By.ID,'state').send_keys("MonteCarlo")
        driver.find_element(By.ID,'zipCode').send_keys("12578")
        driver.find_element(By.ID,'cardType').send_keys("Visa")
        driver.find_element(By.ID,'creditCardNumber').send_keys("5447895654785214")
        Month = driver.find_element(By.ID,'creditCardMonth')
        Month.clear()
        Month.send_keys("11")
        Year = driver.find_element(By.ID,'creditCardYear')
        Year.clear()
        Year.send_keys("2030")
        driver.find_element(By.ID,'nameOnCard').send_keys("Manuel Ledezma")
        submit_button = driver.find_element(By.XPATH,'/html/body/div[2]/form/div[11]/div/input')
        submit_button.click() 
        final = driver.find_element(By.TAG_NAME,'h1')
        assert final.text == "Thank you for your purchase today!"

    def tearDown(self):
        self.driver.close() 


if __name__=='__main__':
    unittest.main (verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name='PurchaseBlazedemo21'))





