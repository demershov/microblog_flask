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
    
    def testOpenYourLastPostIfExist(self):
        bases.Login(bases.username, bases.password)
        
        bases.GoToProfilePage(bases.username, bases.password)
        
        try:
            elem = bases.FindElement(xpaths.getYourLastPostLinkXPath())
            elem.click()
        except exceptions.NoSuchElementException: 
             assert False, "Cancel button was not found"
    
    def testOpenSecondNewsPage(self):
        try:
            elem = bases.FindElement(xpaths.getSecondNewsPageXPath())
            if elem.is_enabled():
                elem.click()
        except exceptions.NoSuchElementException: 
             assert False, "Cancel button was not found"
        
        openFirstPost()        
    
    def testOpenListOfYourPosts(self):
        bases.Login(bases.username, bases.password)

        try:
            elem = bases.FindElement(xpaths.getUserMenuNavbarDropdownXPath())
            elem.click()
        except exceptions.NoSuchElementException: 
             assert False, "Not authenticated"
            
        try:
            elem = bases.FindElement(xpaths.getUsersPostsListLinkXPath())
            elem.click()
        except exceptions.NoSuchElementException: 
             assert False, "Not authenticated"
        
        takeSomeSleep()
        
        assert (bases.driver.current_url == bases.domain + "/user/" + bases.username + "/posts"), "Backtracked to the roots?"
        
        openFirstPost()

        takeSomeSleep()
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()