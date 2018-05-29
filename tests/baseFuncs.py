import unittest
import time
import xpaths
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait


class BaseFunc:
    domain = 'http://127.0.0.1:5000'
    driver = None

    # Existing user data
    username = "naark"
    password = "qwerty1"
    email = "wadernik@mail.ru"

    # def __init__(self, driver):
    #     self.driver = driver
    
    def FindElement(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # FirefoxWebObject
    def GoToLoginPage(self):
        time.sleep(2)
        try:
            elem = self.FindElement(xpaths.getLoginPageXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Login page link does not found"
            return
        assert (self.driver.current_url == BaseFunc.domain + "/login"), "Not the login page"

        return elem
    
    # FirefoxWebObject
    def GoToRegPage(self):
        try:
            elem = self.FindElement(xpaths.getRegPageXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg page link does not found"
            return
        
        assert (self.driver.current_url == BaseFunc.domain + "/register"), "Not the reg page"

        return elem
    
    def GoToEditPage():
        if not bases.CheckIfLoggedIn():
            self.Login(BaseFunc.username, BaseFunc.password)
            assert (self.CheckIfLoggedIn()), "Authentication failed"
        
        try:
            elem = self.FindElement(xpaths.getUserProfileLinkXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Not authenticated"
        
        try:
            elem = self.FindElement(xpaths.getEditPageLinkXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Edit link not found or you are not in your profile"
        
        assert (self.driver.current_url == BaseFunc.domain + "/edit_profile"), "You can't access edit personal info page"

    def Login(self, user, passw):
        elem = self.GoToLoginPage()
        try:
            elem = self.FindElement(xpaths.getLoginInputXPath())
            elem.send_keys(user)
        except exceptions.NoSuchElementException:
            assert False, "Login input element does not found"
            return
        
        try:
            elem = self.FindElement(xpaths.getLoginPassXPath())
            elem.send_keys(passw)
        except exceptions.NoSuchElementException:
            assert False, "Login pass element does not found"
            return
        
        try:
            elem = self.FindElement(xpaths.getLoginButtonXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Login button does not found"
            return

    def CheckIfLoggedIn(self):
        time.sleep(3)
        try:
            self.FindElement(xpaths.getUserProfileLinkXPath())
        except exceptions.NoSuchElementException:
            return False
        return True    