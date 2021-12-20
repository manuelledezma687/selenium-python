from time import sleep


class newticket(object):

    def __init__(self, driver):
        self._driver = driver
        self._url =('https://blazedemo.com/purchase.php')

    def open(self):
        self._driver.get(self._url)


    def name(self,keyword):
        name = self._driver.find_element_by_id('inputName')
        name.send_keys(keyword)
        sleep(1)

    def address(self,keyword):
        adress = self._driver.find_element_by_id('address')
        adress.send_keys(keyword)
        sleep(1)

    def city(self,keyword):
        city = self._driver.find_element_by_id('city')
        city.send_keys(keyword)
        sleep(1)
    
    def state(self,keyword):
        state = self._driver.find_element_by_id('state')
        state.send_keys(keyword)
        sleep(1)
    
    def zipcode(self,keyword):
        zip = self._driver.find_element_by_id('zipCode')
        zip.send_keys(keyword)
        sleep(1)

    def cardtype(self,keyword):
        cdtype = self._driver.find_element_by_id('cardType')
        cdtype.send_keys(keyword)
        sleep(1)
    
    def creditcard(self,keyword):
        cdnumber = self._driver.find_element_by_id('creditCardNumber')
        cdnumber.send_keys(keyword)
        sleep(1)

    def month(self,keyword):
        month = self._driver.find_element_by_id('creditCardMonth')
        month.clear()
        month.send_keys(keyword)
        sleep(1)

    def year(self,keyword):
        year = self._driver.find_element_by_id('creditCardYear')
        year.send_keys(keyword)
        sleep(1)
    
    def nameoncard (self,keyword):
        nameoncard = self._driver.find_element_by_id('nameOnCard')
        nameoncard.send_keys(keyword)
        sleep(1)

    def checkbox (self):
        checkbox = self._driver.find_element_by_name('rememberMe')
        checkbox.click()
        sleep(1)

    def click_submit(self):
        enviar = self._driver.find_element_by_xpath('/html/body/div[2]/form/div[11]/div/input')
        enviar.click()


    def confirmshop(self):
        final = self._driver.find_element_by_tag_name('h1')
        assert final.text == "Thank you for your purchase today!"