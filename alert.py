import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


class CompareProducts(unittest.TestCase):

	def setUp(self):
		s = ChromeService(executable_path='chromedriver')
		self.driver = webdriver.Chrome(service=s)
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get("http://demo-store.seleniumacademy.com/")
	
	def test_compare_products_removal_alert(self):
		driver = self.driver
		search_field = driver.find_element(By.ID,'search')
		search_field.clear()
		search_field.send_keys('tee')
		search_field.submit()

		driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/ul/li[2]/a').click()
		driver.find_element(By.LINK_TEXT,'Clear All').click()
		
		#alert = wait.until(expected_conditions.alert_is_present())
		#text = alert.text
		#alert.accept()
		#self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

	def tearDown(self):
		self.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2,)
