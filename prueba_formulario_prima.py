import unittest
from selenium import webdriver
from time import sleep

class NuevoTestPage(unittest.TestCase):  

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path  = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.prismamediosdepago.com/contacto') 
    

    def test_contact_form (self):
        driver =self.driver
        first_name = driver.find_element_by_id('edit-nombre')
        last_name = driver.find_element_by_id('edit-apellido')
        phone = driver.find_element_by_id('edit-telefono')
        email = driver.find_element_by_id('edit-correo-electronico')
        Factory = driver.find_element_by_id('edit-empresa')
        message = driver.find_element_by_id('edit-mensaje')
        submit_button = driver.find_element_by_id('edit-submit')

        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and phone.is_enabled()
        and email.is_enabled()
        and Factory.is_enabled()
        and message.is_enabled()
        and submit_button.is_enabled())

        
        first_name.send_keys("Robert")
        last_name.send_keys("Gomez")
        phone.send_keys("1148759478")
        email.send_keys("mm@gmail.com")
        Factory.send_keys("tstt001")
        message.send_keys("Mensaje de muestra")
        submit_button.click() 
        sleep (3)

    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.close() 


if __name__=='__main__':
    unittest.main (verbosity=2, )





