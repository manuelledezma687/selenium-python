from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner 
from Blazedemo import NuevoTestPage
from SauceDemo import Saucetest

TestLoader().loadTestsFromTestCase(NuevoTestPage)
TestLoader().loadTestsFromTestCase(Saucetest)

smoke_test = TestSuite([NuevoTestPage, Saucetest])

kwargs = {
    "output": 'smoke-test'
    }


runner = HTMLTestRunner(**kwargs)

#corro el rurner con la suite de prueba
runner.run(smoke_test) 

