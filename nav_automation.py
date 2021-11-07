import unittest
from selenium import webdriver


class googletest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        field = driver.find_element_by_name('q')
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