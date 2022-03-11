import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


class AssertionsTest(unittest.TestCase):

	def setUp(self):
		s = ChromeService(executable_path='chromedriver')
		self.driver = webdriver.Chrome(service=s)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get("http://demo.onestepcheckout.com/")

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))

	def tearDown(self):
		self.driver.quit()

	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
	def	is_element_present(self, how, what):
		try:  #busca los elementos según el parámetro
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True

if __name__=="__main__":
    unittest.main(verbosity=2,)
