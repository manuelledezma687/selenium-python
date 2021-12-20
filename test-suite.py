from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner 
from nav_automation import googletest
from SauceDemo import Saucetest
from assertions02 import demosauce 
from assertions01 import test_assertion
from newdemo import newdemo

test1 = TestLoader().loadTestsFromTestCase(googletest)
test2 = TestLoader().loadTestsFromTestCase(Saucetest)
test3 = TestLoader().loadTestsFromTestCase(demosauce)
test4 = TestLoader().loadTestsFromTestCase(test_assertion)
test5 = TestLoader().loadTestsFromTestCase(newdemo)

#Construccion de suite de pruebas
smoke_test = TestSuite([test1, test2, test3, test4, test5])

kwargs = {
    "output": 'smoke-report'
    }

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

