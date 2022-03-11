
from selenium.webdriver.common.by import By


class newTicket(object):

    def __init__(self, driver):
        self._driver = driver
        self._url =('https://blazedemo.com/purchase.php')

    def open(self):
        self._driver.get(self._url)

    def name(self,keyword):
        name = self._driver.find_element(By.ID,'inputName')
        name.send_keys(keyword)

    def address(self,keyword):
        adress = self._driver.find_element(By.ID,'address')
        adress.send_keys(keyword)

    def city(self,keyword):
        city = self._driver.find_element(By.ID,'city')
        city.send_keys(keyword)
    
    def state(self,keyword):
        state = self._driver.find_element(By.ID,'state')
        state.send_keys(keyword)
    
    def zipcode(self,keyword):
        zip = self._driver.find_element(By.ID,'zipCode')
        zip.send_keys(keyword)

    def cardtype(self,keyword):
        cdtype = self._driver.find_element(By.ID,'cardType')
        cdtype.send_keys(keyword)
    
    def creditcard(self,keyword):
        cdnumber = self._driver.find_element(By.ID,'creditCardNumber')
        cdnumber.send_keys(keyword)

    def month(self,keyword):
        month = self._driver.find_element(By.ID,'creditCardMonth')
        month.clear()
        month.send_keys(keyword)

    def year(self,keyword):
        year = self._driver.find_element(By.ID,'creditCardYear')
        year.send_keys(keyword)
    
    def nameoncard (self,keyword):
        nameoncard = self._driver.find_element(By.ID,'nameOnCard')
        nameoncard.send_keys(keyword)


    def checkbox (self):
        checkbox = self._driver.find_element(By.ID,'rememberMe')
        checkbox.click()

    def click_submit(self):
        enviar = self._driver.find_element(By.XPATH,'/html/body/div[2]/form/div[11]/div/input')
        enviar.click()


    def confirmshop(self):
        final = self._driver.find_element(By.TAG_NAME,'h1')
        assert final.text == "Thank you for your purchase today!"