import unittest
from selenium import webdriver
from prismapage1 import prismapage
from pyunitreport import HTMLTestRunner


class testprisma(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path  = '../chromedriver')
     
    def testformulariocompleto(self):
        
        prisma = prismapage(self.driver)
        prisma.open()
        prisma.name("jorge")
        prisma.lastname("alvarez")
        prisma.phone("125454632")
        prisma.email ("mmm@qa.team")
        prisma.factory("walrus")
        prisma.message("sadasdsa")
        prisma.click_submit()



    def testsinemail(self):
        
        prisma = prismapage(self.driver)
        prisma.open()
        prisma.name("jorge")
        prisma.lastname("alvarez")
        prisma.phone("125454632")
        prisma.factory("walrus")
        prisma.message("sadasdsa")
        prisma.click_submit()


    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output="reportes", report_name="POM CONTACT-MAIN"))