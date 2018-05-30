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

def checkOnWrongUsername():
    time.sleep(3)
    try:
        bases.FindElement(xpaths.getLoginWrongUsernameMessageXPath())
    except exceptions.NoSuchElementException:
        assert False, "Username is correct, but it shouldn't be"

    assert (bases.driver.current_url == bases.domain + "/login"), "Authentication successfully completed, but it shouldn't be"

def goToResetPassEmailPage():
    try:
        elem = bases.FindElement(xpaths.getResetPasswordLinkXPath())
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Forgot password link not found"
    
    assert (bases.driver.current_url == bases.domain + "/reset_password_request"), "Not the reseting password link"

def addEmail(text):
    try:
        elem = bases.FindElement(xpaths.getResetEmailConfirmInputXPath())
        elem.send_keys(text)
    except exceptions.NoSuchElementException:
        assert False, "Email input field not found"

def submitEmail():
    try:
        elem = bases.FindElement(xpaths.getResetSubmitButtonXPath())
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Submit button not found"

def submitNewPassword(text, rightCase):
    try:
        elem = bases.FindElement("//*[@id='password']")
        elem.send_keys(text)
    except exceptions.NoSuchElementException:
        assert False, "Password input field not found"
    
    try:
        elem = bases.FindElement("//*[@id='password2']")
        if not rightCase:
            elem.send_keys(text + "123")
        else:
            elem.send_keys(text)
    except exceptions.NoSuchElementException:
        assert False, "Confirm pass input field not found"
    
    try:
        elem = bases.FindElement("//*[@id='submit']")
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Confirm pass input field not found"

def checkMail():
    bases.driver.implicitly_wait(10)
    bases.driver.get("https://mail.ru/")

    try:
        elem = bases.FindElement("//*[@id='mailbox:login']")
        elem.send_keys("l3g4_mania")
    except exceptions.NoSuchElementException:
        assert False, "Email input field not found"
    
    try:
        elem = bases.FindElement("//*[@id='mailbox:password']")
        elem.send_keys("b3rserkeR")
    except exceptions.NoSuchElementException:
        assert False, "Pass input field not found"
    
    try:
        elem = bases.FindElement("//*[@id='mailbox:submit']/input")
        elem.click()
    except exceptions.NoSuchElementException:
        assert False, "Login button not found"
    
    try:
        elem = bases.FindElement("//*[@id='b-letters']/div/div[2]/div/div[2]/div[1]/div/a/div[4]/div[3]/div[2]")
    except exceptions.NoSuchElementException:
        assert False, "Login button not found"
    
    if elem.text != "degalweb@gmail.com":
        assert False, "Message not found"
    
    elem.click()
    try:
        elem = bases.driver.find_element_by_link_text("кликните по ссылке")
        # elem = bases.FindElement("//*[@id='style_15276508360000000399_BODY']/div/p[2]/a")
        newUrl = elem.get_attribute("href")
        bases.driver.implicitly_wait(10)
        bases.driver.get(newUrl)
    except exceptions.NoSuchElementException:
        assert False, "Reset link not found"

class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver
    
    def testResetPassword1(self):
        bases.GoToLoginPage()
        goToResetPassEmailPage()
        addEmail("l3g4_mania@mail.ru")
        submitEmail()
        checkMail()
        submitNewPassword("qwerty123", True)
    
    def testResetPassword2(self):
        bases.GoToLoginPage()
        goToResetPassEmailPage()
        addEmail("l3g4_mania@mail.ru")
        submitEmail()
        checkMail()
        submitNewPassword("qwerty5", False)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()