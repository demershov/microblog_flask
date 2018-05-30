import unittest
import time
import random
import xpaths
from baseFuncs import BaseFunc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

bases = BaseFunc()

def takeSleep():
    time.sleep(4)

def getOrCreateWebdriver():
    bases.driver = webdriver.Firefox()
    return bases.driver

def addTextQuery(text):
    try:
        elem = bases.FindElement(xpaths.getSearchInputFieldXPath())
        elem.clear()
        elem.send_keys(text)
    except exceptions.NoSuchElementException:
        assert False, "Search input is unavailable"

def submitQuery():
    try:
        elem = bases.FindElement(xpaths.getSearchSubmitButtonXPath())
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Search button is unavailable"

class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver

        bases.Login(bases.username, bases.password)
        if not bases.CheckIfLoggedIn():
                bases.CheckWhyAuthFailed()
    
    def testCasualSearch1(self):
        addTextQuery("Selenium")
        submitQuery()
        bases.openFirstPost()
        takeSleep()
    
    def testCasualSearch2(self):
        addTextQuery("asdasdasdasd")
        submitQuery()
        bases.openFirstPost()
        takeSleep()
    
    def testCasualSearch3(self):
        addTextQuery("ＯＤＥＶＡＥＴ")
        submitQuery()
        bases.openFirstPost()
        takeSleep()
    
    def testCasualSearch4(self):
        addTextQuery("")
        submitQuery()
        bases.openFirstPost()
        takeSleep()
    
    def testCasualSearch5(self):
        addTextQuery("afasfafafasfafafasfafafasfafaf")
        submitQuery()
        bases.openFirstPost()
        takeSleep()
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()