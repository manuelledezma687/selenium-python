import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


class googleTest(unittest.TestCase):

    def setUp(self):
        s = ChromeService(executable_path='chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        field = driver.find_element(By.NAME,'q')
        field.clear()
        field.send_keys("hola")
        field.submit()
        driver.back()
        driver.forward()
        driver.refresh()


    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2 )