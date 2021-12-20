class homeblaze(object):

    def __init__(self, driver):
        self._driver = driver
        self._url =('https://blazedemo.com/')
    

    def point(self, keyword):
        point = self._driver.find_element_by_name('toPort')
        point.send_keys(keyword)


    def destiny(self, keyword):
        lname = self._driver.find_element_by_name('fromPort')
        lname.send_keys(keyword)

    
    def click_submit(self):
        submit = self._driver.find_element_by_css_selector('body > div.container > form > div > input')
        submit.submit()

    def select_destiny(self,keyword):
        destiny = self.driver.find_element_by_class_name('btn btn-small')
        destiny.send_keys(keyword)

    def open(self):
        self._driver.get(self._url)