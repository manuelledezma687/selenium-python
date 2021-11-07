import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
class mercadolibre_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get ("https://www.mercadolibre.com/")
        

    def test_mercadolibre(self):
        driver = self.driver
        driver.find_element_by_id("CL").click()
        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys("Play station 4")
        search_field.submit()

    
        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)   
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]').text
            
            prices.append(article_price)

        print(articles, prices)
        sleep(5)


    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.close() 

if __name__ == "__main__":
    unittest.main (verbosity=2, )

