from pyunitreport import HTMLTestRunner
from unittest import TestSuite,TestLoader
from find_element_practice3 import testphptravels
from SauceDemo import Saucetest

test1 = TestLoader().loadTestsFromTestCase(testphptravels)
test2 = TestLoader().loadTestsFromTestCase(Saucetest)


test_suite = TestSuite([test1,test2])

kwargs = {

    "output":"test_suite1"
}

runner = HTMLTestRunner(**kwargs)

runner.run(test_suite)