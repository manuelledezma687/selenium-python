import unittest
from selenium import webdriver


class retoblazedemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get ('https://www.blazedemo.com/reserve.php')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_blazedemo(self):
        driver = self.driver
        list = driver.find_element_by_css_selector("body")
        vuelos = list.find_elements_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[1]/input')
        self.assertEqual(1,len(vuelos))

    

    def tearDown(self):
        self.driver.close()


if __name__=="__main__":
    unittest.main(verbosity =2)