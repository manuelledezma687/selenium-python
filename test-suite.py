from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner 
from nav_automation import googletest
from SauceDemo import Saucetest
from newdemo import newdemo

test1 = TestLoader().loadTestsFromTestCase(googletest)
test2 = TestLoader().loadTestsFromTestCase(Saucetest)
test3 = TestLoader().loadTestsFromTestCase(newdemo)

#Construccion de suite de pruebas
smoke_test = TestSuite([test1, test2, test3])

kwargs = {
    "output": 'smoke-report'
    }

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

