import unittest
import time
import random
import xpaths
from baseFuncs import BaseFunc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

bases = BaseFunc()

def getOrCreateWebdriver():
    bases.driver = webdriver.Firefox()
    return bases.driver

def saveChanges():
    try:
        element = bases.FindElement(xpaths.getSubmitChangesButtonXPath())
        element.click()
    except exceptions.NoSuchElementException:
        assert False, "Submit button was not found"

class SiteTest(unittest.TestCase):

    # Setup
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver
    
    # Positives
    def testCancelEdit():
        bases.GoToEditPage()

        try:
            element = bases.FindElement(xpaths.getCancelButtonXPath())
            element.click()
        except exceptions.NoSuchElementException:
            assert False, "Cancel button was not found"
        
        assert (bases.driver.current_url == bases.domain + "/user/" + bases.username), "Cancel button backtracked you somewhere to the roots"
    
    def testSaveWithoutChanges():
        bases.GoToEditPage()

        try:
            element = bases.FindElement(xpaths.getCancelButtonXPath())
            element.click()
        except exceptions.NoSuchElementException:
            assert False, "Cancel button was not found"
        
        assert (bases.driver.current_url == bases.domain + "/user/" + bases.username), "Cancel button backtracked you somewhere to the roots"


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()