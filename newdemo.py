import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class newDemo(unittest.TestCase):

    def setUp(self):
        s = ChromeService(executable_path='chromedriver')
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demoqa.com/alerts")

    def test_newdemo(self):
        driver = self.driver
        driver.find_element(By.ID,'confirmButton').click()
        alert = driver.switch_to_alert()
        alert_text = alert.text
        self.assertEqual('Do you confirm action?', alert_text)
        alert.accept()

    def tearDown(self):
        self.driver.close() 

if __name__=="__main__":
    unittest.main(verbosity=2,)

