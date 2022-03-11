import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from pages.fromshop import newTicket
from selenium.webdriver.chrome.service import Service as ChromeService


class testblaze(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        s = ChromeService(executable_path='chromedriver')
        cls.driver = webdriver.Chrome(service=s)

    def testpurchase(self):
        newsale = newTicket(self.driver)
        newsale.open()
        newsale.name('alejandro')
        newsale.address('asdasdasd')
        newsale.city('vanuatu')
        newsale.state('Australia')
        newsale.zipcode("10481")
        newsale.cardtype('Visa')
        newsale.creditcard("4242424242424")
        newsale.month('11')
        newsale.year('2018')
        newsale.nameoncard('manuel ledeadaz')
        newsale.checkbox()
        newsale.field_assertion()
        newsale.click_submit()
        newsale.confirmshop()

    @classmethod
    def tearDown(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output="reportes", report_name="blazedemopom"))
