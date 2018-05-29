import unittest
import time
import xpaths
import random
import sys
import os
#sys.path.append('E:/Github/aderkin/microblog_flask-dmitry/tests/')
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import login.xpaths
import login.login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait

domain = 'http://127.0.0.1:5000'
driver = None

# Data for casual login
username = "naark"
password = "qwerty1"

def getOrCreateWebdriver():
    global driver
    driver = webdriver.Firefox()
    return driver

def findElement(xpath):
        return driver.find_element_by_xpath(xpath)

def doLogin():
    try:
        elem = findElement(login.xpaths.getLoginInputXPath())
        elem.send_keys(username)
    except exceptions.NoSuchElementException:
        # assert False, "Login input element does not found"
        return False
    
    try:
        elem = findElement(login.xpaths.getLoginPassXPath())
        elem.send_keys(password)
    except exceptions.NoSuchElementException:
        # assert False, "Login pass element does not found"
        return False
    
    try:
        elem = findElement(login.xpaths.getLoginButtonXPath())
        elem.click()
    except exceptions.NoSuchElementException:
        # assert False, "Login button does not found"
        return False
    
    return True

def takeSomeSleep():
    time.sleep(5)

class SiteTest(unittest.TestCase):

    # Setup
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(12)
        global domain
        self.driver.get(domain)

    # Open first (the newest by date) post on the page and then to poster's profile
    def testOpenFirstPostOnPage(self):
        try:
            elem = findElement(xpaths.getFirstPostPageXPath())
            newUrl = elem.get_attribute("href")
            elem.click()
            driver.set_page_load_timeout(10)
            assert (driver.current_url == newUrl), "Wrong link provided"

        except exceptions.NoSuchElementException:
            assert False, "No posts found"
            return

        try:
            elem = findElement(xpaths.getPosterProfileLinkFromPost())
            elem.click()
            driver.set_page_load_timeout(10)
        except exceptions.NoSuchElementException:
            assert False, "No poster's link found"
            return
        
        login.login.driver = driver
        login.login.checkIfLoggedIn()

    
    # Do the same, but login at the end
    def testLoginAfterClickProfileLink(self):
        try:
            elem = findElement(xpaths.getFirstPostPageXPath())
            newUrl = elem.get_attribute("href")
            elem.click()
            driver.set_page_load_timeout(10)
            assert (driver.current_url == newUrl), "Wrong link provided"

        except exceptions.NoSuchElementException:
            assert False, "No posts found"
            return

        try:
            elem = findElement(xpaths.getPosterProfileLinkFromPost())
            elem.click()
            driver.set_page_load_timeout(10)
        except exceptions.NoSuchElementException:
            assert False, "No poster's link found"
            return
        
        assert doLogin(), "Login failed"
    
        takeSomeSleep()
    
    # Open login page, log in, click first post, open poster's profile
    def testOpenProfileWhileSignedIn(self):
        login.login.driver = driver
        elem = login.login.GoToLoginPage(login.xpaths)

        assert doLogin(), "Login failed"

        self.testOpenFirstPostOnPage()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()