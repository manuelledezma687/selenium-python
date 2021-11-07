import unittest
from selenium import webdriver


class newdemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://demoqa.com/alerts")

    def test_newdemo(self):
        driver = self.driver
        driver.find_element_by_id('confirmButton').click()
        alert = driver.switch_to_alert()
        alert_text = alert.text
        self.assertEqual('Do you confirm action?', alert_text)
        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.close() 

if __name__ == "__main__":
	unittest.main(verbosity = 2)
