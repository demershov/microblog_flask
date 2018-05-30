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

def openNewPostPage():
    bases.Login(bases.username, bases.password)

    if not bases.CheckIfLoggedIn():
        bases.CheckWhyAuthFailed()
    
    try:
        elem = bases.FindElement(xpaths.getWriteNewPostLinkXPath())
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Not authenticated"

# TODO: Improve these 2 funcs
def addTitle(text):
    if not bases.CheckIfLoggedIn():
        bases.CheckWhyAuthFailed()
    
    try:
        elem = bases.FindElement(xpaths.getPostTitleInputFieldXPath())
        elem.clear()
        elem.send_keys(text)
    except exceptions.NoSuchElementException:
        assert False, "Title input is unavailable"

def addContent(text):
    if not bases.CheckIfLoggedIn():
        bases.CheckWhyAuthFailed()
    
    try:
        bases.driver.switch_to.frame(bases.driver.find_element_by_tag_name("iframe"))
        elem = bases.driver.find_element_by_xpath(xpaths.getPostTextFieldXPath())
        bases.driver.execute_script("arguments[0].textContent = arguments[1];", elem, text)        
        bases.driver.switch_to.default_content()
    except exceptions.NoSuchElementException:
        assert False, "Iframe content area is unavailable"

def sumbitPost():
    try:
        elem = bases.FindElement(xpaths.getSubmitButtonXPath())
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Submit button is unavailable"

def checkIfPostSubmited():
    time.sleep(3)
    try:
        elem = bases.FindElement(xpaths.getTitleErrorMessageXPath())
        assert len(elem.text) <= 0, "Title error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass
    
    try:
        elem = bases.FindElement(xpaths.getContentErrorMessageXPath())
        assert len(elem.text) <= 0, "Content error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass

def checkOnTitleFailTest():
    time.sleep(3)
    try:
        bases.FindElement(xpaths.getTitleErrorMessageXPath())
    except exceptions.NoSuchElementException:
        assert False, "Title is correct, but it shouldn't be"

    assert (bases.driver.current_url == bases.domain + "/add_post"), "Backtracked to the roots, but shouldn't have been"

def checkOnContentFailTest():
    time.sleep(3)
    try:
        bases.FindElement(xpaths.getContentErrorMessageXPath())
    except exceptions.NoSuchElementException:
        assert False, "Content is correct, but it shouldn't be"

    assert (bases.driver.current_url == bases.domain + "/add_post"), "Backtracked to the roots, but shouldn't have been"


class SiteTest(unittest.TestCase):

    # Setup
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver
    
    def testCasualPost1(self):
        openNewPostPage()
        addTitle("Test title // selenium")
        addContent("Selenium is love. Selenium is life.")
        sumbitPost()
        checkIfPostSubmited
    
    def testCasualPost2(self):
        openNewPostPage()
        addTitle("Test title // selenium")
        addContent("Selenium is love. Selenium is life. Selenium is love. Selenium is life."\
                   "Selenium is love. Selenium is life. Selenium is love. Selenium is life."\
                   "Selenium is love. Selenium is life. Selenium is love. Selenium is life.")
        sumbitPost()
        checkIfPostSubmited()
    
    def testBlankFields(self):
        openNewPostPage()
        sumbitPost()
        checkOnTitleFailTest()
        checkOnContentFailTest()
    
    def testBlankContentField(self):
        openNewPostPage()
        addTitle("Test title // selenium")
        sumbitPost()
        checkOnContentFailTest()
    
    def testTitleLessThan10(self):
        openNewPostPage()
        addTitle("Test")
        addContent("Selenium is love. Selenium is life.")
        sumbitPost()
        checkOnTitleFailTest()
    
    def testTitleGreaterThan255(self):
        openNewPostPage()
        addTitle("TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest"\
                 "TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest"\
                 "TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest")
        addContent("Selenium is love. Selenium is life.")
        sumbitPost()
        checkOnTitleFailTest()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()