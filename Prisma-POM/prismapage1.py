
from time import sleep


class prismapage(object):

    def __init__(self, driver):
        self._driver = driver
        self._url =('https://www.prismamediosdepago.com/contacto')
    

    def name(self, keyword):
        name = self._driver.find_element_by_id('edit-nombre')
        name.send_keys(keyword)
        sleep(1)

    def lastname(self, keyword):
        lname = self._driver.find_element_by_id('edit-apellido')
        lname.send_keys(keyword)
        sleep(1)
    
    def phone(self, keyword):
        lname = self._driver.find_element_by_id('edit-telefono')
        lname.send_keys(keyword)
        sleep(1)

    def email(self, keyword):
        lname = self._driver.find_element_by_id('edit-correo-electronico')
        lname.send_keys(keyword)
        sleep(1)

    def factory(self, keyword):
        lname = self._driver.find_element_by_id('edit-empresa')
        lname.send_keys(keyword)
        sleep(1)

    def message(self, keyword):
        lname = self._driver.find_element_by_id('edit-mensaje')
        lname.send_keys(keyword)
        sleep(1)

    def click_submit(self):
        input_field = self._driver.find_element_by_id('edit-submit')
        input_field.submit()



    def open(self):
        self._driver.get(self._url)



