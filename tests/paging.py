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

def takeSomeSleep():
    time.sleep(5)

def openFirstPost():
    try:
        elem = bases.FindElement(xpaths.getFirstPostPageXPath())
        newUrl = elem.get_attribute("href")
        elem.click()
        bases.driver.set_page_load_timeout(10)
        assert (bases.driver.current_url == newUrl), "Wrong link provided"
    except exceptions.NoSuchElementException:
        assert False, "No posts found"
        return

def openPostersProfile():
    try:
        elem = bases.FindElement(xpaths.getPosterProfileLinkFromPostXPath())
        elem.click()
        bases.driver.set_page_load_timeout(10)
    except exceptions.NoSuchElementException:
        assert False, "No poster's link found"
        return

class SiteTest(unittest.TestCase):

    # Setup
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver

    # Open first (the newest by date) post on the page and then to poster's profile
    def testOpenPostersProfile(self):
        openFirstPost()
        openPostersProfile()

    # Do the same, but login at the end
    def testLoginAfterClickProfileLink(self):
        openFirstPost()
        openPostersProfile()
        
        bases.Login(bases.username, bases.password)
        #assert (bases.CheckIfLoggedIn()), "Authentication failed"
        if not bases.CheckIfLoggedIn():
                bases.CheckWhyAuthFailed()
    
        takeSomeSleep()
    
    # Open login page, log in, click first post, open poster's profile
    def testOpenProfileWhileSignedIn(self):
        bases.Login(bases.username, bases.password)
        #assert (bases.CheckIfLoggedIn()), "Authentication failed"
        if not bases.CheckIfLoggedIn():
                bases.CheckWhyAuthFailed()

        openFirstPost()

        openPostersProfile()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()