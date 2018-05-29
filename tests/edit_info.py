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
    def testCancelEdit(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getCancelButtonXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Cancel button was not found"
        
        assert (bases.driver.current_url == bases.domain + "/user/" + bases.username), "Cancel button backtracked you somewhere to the roots"
    
    def testSaveWithoutChanges(self):
        bases.GoToEditPage(bases.username, bases.password)

        saveChanges()
        
        assert (bases.driver.current_url == bases.domain + "/edit_profile"), "Save button backtracked you somewhere to the roots"
        
        try:
            elem = bases.FindElement(xpaths.getUsernameXpath())
            assert (bases.username == elem.text), "Username changed, but shouldn't have been"
        except exceptions.NoSuchElementException:
            assert False, "Username field not found"

    def testAppendToUsername(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditUsernameFieldXPath())
            elem.send_keys("naark1")
        except exceptions.NoSuchElementException:
            assert False, "Username field not found"
    
        saveChanges()

        try:
            elem = bases.FindElement(xpaths.getUsernameXpath())
            assert (elem.text == bases.username + "naark1"), "Username does not changed"
            bases.username += "naark1"
        except exceptions.NoSuchElementException:
            assert False, "Not authenticated"
    
    def testChangeUsernameToNew(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditUsernameFieldXPath())
            elem.clear()
            elem.send_keys("naark1")
        except exceptions.NoSuchElementException:
            assert False, "Username field not found"
        
        saveChanges()

        try:
            elem = bases.FindElement(xpaths.getUsernameXpath())
            assert (elem.text == "naark1"), "Username does not changed"
            bases.username = "naark1"
        except exceptions.NoSuchElementException:
            assert False, "Not authenticated"
    
    def testChangeToNewEmail(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditEmailFieldXPath())
            elem.clear()
            elem.send_keys("test" + str(random.randint(1, 60)) + "@login.com")
        except exceptions.NoSuchElementException:
            assert False, "Email field not found"
        
        saveChanges()

        try:
            elem = bases.FindElement(xpaths.getEditEmailErrorMessage())
            assert len(elem.text) <= 0, "Email error message appears: " + elem.text
        except exceptions.NoSuchElementException:
            pass
    
    def testAddNewAboutInfo(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditAboutFieldXPath())
            elem.clear()
            elem.send_keys("test")
        except exceptions.NoSuchElementException:
            assert False, "Email field not found"

        saveChanges()

        try:
            elem = bases.FindElement(xpaths.getEditAboutInfoErrorMessage())
            assert len(elem.text) <= 0, "Email error message appears: " + elem.text
        except exceptions.NoSuchElementException:
            pass
    
    def testAddBlankAboutInfo(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditAboutFieldXPath())
            elem.clear()
        except exceptions.NoSuchElementException:
            assert False, "Email field not found"

        saveChanges()

        try:
            elem = bases.FindElement(xpaths.getEditAboutInfoErrorMessage())
            assert len(elem.text) <= 0, "Email error message appears: " + elem.text
        except exceptions.NoSuchElementException:
            pass
    
    # #Negatives
    def testChangeToExistedUsername(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditUsernameFieldXPath())
            elem.clear()
            elem.send_keys("susan")
        except exceptions.NoSuchElementException:
            assert False, "Username field not found"
        
        saveChanges()

        try:
            bases.FindElement(xpaths.getEditLoginErrorMessage())
            # assert len(elem.text) <= 0, "Username error message appears: " + elem.text
        except exceptions.NoSuchElementException:
            assert False, "Username changed, but shouldn't have been"

    
    def testChangeToExistedEmail(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditEmailFieldXPath())
            elem.clear()
            elem.send_keys("test@login.com")
        except exceptions.NoSuchElementException:
            assert False, "Email field not found"
        
        saveChanges()
        time.sleep(4)

        try:
            elem = bases.FindElement(xpaths.getEditEmailErrorMessage())
            # assert len(elem.text) <= 0, "Email error message appears: " + elem.text
        except exceptions.NoSuchElementException:
            assert False, "Email changed, but shouldn't have been"

    def testAddNewAboutInfoWithLargeInput(self):
        bases.GoToEditPage(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getEditAboutFieldXPath())
            elem.clear()
            elem.send_keys("testtesttesttesttesttesttesttesttesttesttesttest"\
            "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttes"\
            "testtesttesttesttesttesttesttesttesttesttesttesttest")
        except exceptions.NoSuchElementException:
            assert False, "Email field not found"

        saveChanges()

        try:
            bases.FindElement(xpaths.getEditAboutInfoErrorMessage())
        except exceptions.NoSuchElementException:
            assert False, "About info was saved, but shouldn't have been"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()