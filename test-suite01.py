from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from nav_automation import googletest
from newdemo import newdemo


helloworld = TestLoader().loadTestsFromTestCase(newdemo)
helloworld2 = TestLoader().loadTestsFromTestCase(googletest)

test_suite = TestSuite([helloworld,helloworld2])

kwargs = {
    "output": "test-suite"

          }

runner = HTMLTestRunner(**kwargs)
runner.run(test_suite)
