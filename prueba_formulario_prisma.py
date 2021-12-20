import unittest
from selenium import webdriver
from openpyxl import load_workbook

class NuevoTestPage(unittest.TestCase):  
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path  = './chromedriver')


    def test_contact_form (self):
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.prismamediosdepago.com/contacto') 
        filesheet = "./contactos.xlsx"
        wb = load_workbook(filesheet)
        names = wb.get_sheet_names()
        print(names)
        contact = wb.get_sheet_by_name('Hoja1')
        wb.close()

        for i in range(1,8):
            driver = self.driver
            first_name,last_name,phone,email,Factory,message =contact [f'A{i}:F{i}'][0]
            driver.find_element_by_id('edit-nombre').send_keys(first_name.value)
            driver.find_element_by_id('edit-apellido').send_keys(last_name.value)
            driver.find_element_by_id('edit-telefono').send_keys(phone.value)
            driver.find_element_by_id('edit-correo-electronico').send_keys(email.value)
            driver.find_element_by_id('edit-empresa').send_keys(Factory.value)
            driver.find_element_by_id('edit-mensaje').send_keys(message.value)
            driver.find_element_by_id('edit-submit').click()   
            self.driver.close() 

    @classmethod
    def tearDown(cls):
        cls.driver.implicitly_wait(20)
        


if __name__=='__main__':
    unittest.main (verbosity=2, )





