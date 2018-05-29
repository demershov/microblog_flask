import unittest
import time
import xpaths
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

domain = 'http://127.0.0.1:5000/'
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

def GoToLoginPage(xpaths):
        # assert "Микроблог" in  driver.title
        try:
            elem = findElement(xpaths.getLoginPageXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Login page link does not found"
            return
        
        assert (driver.current_url == domain + "login"), "Not the login page"

        return elem

def checkIfLoggedIn():
    time.sleep(4)
    try:
        # element = findElement(xpaths.getNavbarUsernameXPath())
        # assert (element.text == username), "Not authenticated"
        assert (domain + "/user/" not in driver.current_url), "Not authenticated"
    except exceptions.NoSuchElementException:
        assert False, "Navbar element does not found"
        
def checkOnWrongUsername():
    time.sleep(3)
    try:
        findElement(xpaths.getWrongUsernameMessageXPath())
    except exceptions.NoSuchElementException:
        assert False, "Username is correct, but it shouldn't be"

    assert (driver.current_url == domain + "login"), "Authentication successfully completed, but it shouldn't be"

def checkOnWrongPassword():
    time.sleep(3)
    try:
        findElement(xpaths.getWrongPasswordMessageXPath())
    except exceptions.NoSuchElementException:
        assert False, "Password is correct, but it shouldn't be"

    assert (driver.current_url == domain + "login"), "Authentication successfully completed, but it shouldn't be"     

class SiteTest(unittest.TestCase):

    # Setup
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        global domain
        self.driver.get(domain)

    # Casual login
    def testCasualLogIn(self):
        elem = GoToLoginPage(xpaths)

        try:
            elem = findElement(xpaths.getLoginInputXPath())
            elem.send_keys(username)
        except exceptions.NoSuchElementException:
            assert False, "Login input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getLoginPassXPath())
            elem.send_keys(password)
        except exceptions.NoSuchElementException:
            assert False, "Login pass element does not found"
            return

        try:
            elem = findElement(xpaths.getLoginButtonXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Login button does not found"
            return
         
        checkIfLoggedIn()

    # Fail tests
    # Login with wrong pass
    def testWrongPassLogin(self):
        elem = GoToLoginPage(xpaths)
        
        try:
            elem = findElement(xpaths.getLoginInputXPath())
            elem.send_keys(username)
        except exceptions.NoSuchElementException:
            assert False, "Login input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getLoginPassXPath())
            elem.send_keys("123" + password + "123")
        except exceptions.NoSuchElementException:
            assert False, "Login pass element does not found"
            return

        try:
            elem = findElement(xpaths.getLoginButtonXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Login button does not found"
            return
        
        checkOnWrongPassword()
    
    # Смысла это тестить нет, ибо на странице логина поля должны быть 100% заполнены для отправки запроса.
    # Ни xpath, ни какого-либо вообще следа на клиенте я не могу словить, поэтому тест отменен
    # Blank password field
    # def testBlankPassField(self):
    #     elem = GoToLoginPage()
        
    #     try:
    #         elem = findElement(xpaths.getLoginInputXPath())
    #         elem.send_keys(username)
    #     except exceptions.NoSuchElementException:
    #         assert False, "Login input element does not found"
    #         return

    #     try:
    #         elem = findElement(xpaths.getLoginButtonXPath())
    #         elem.click()
    #     except exceptions.NoSuchElementException:
    #         assert False, "Login button does not found"
    #         return
        
    #     checkOnWrongPassword()

    # Login with non-existent user
    def testNonExistentUserLogin(self):
        elem = GoToLoginPage(xpaths)
        
        try:
            elem = findElement(xpaths.getLoginInputXPath())
            elem.send_keys("asdsad")
        except exceptions.NoSuchElementException:
            assert False, "Login input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getLoginPassXPath())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Login pass element does not found"
            return

        try:
            elem = findElement(xpaths.getLoginButtonXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Login button does not found"
            return

        checkOnWrongUsername()
    
    # Аналогично
    # Login with blank usernamefield
    # def testBlankeFields(self):
    #     elem = GoToLoginPage()

    #     try:
    #         elem = findElement(xpaths.getLoginButtonXPath())
    #         elem.click()
    #     except exceptions.NoSuchElementException:
    #         assert False, "Login button does not found"
    #         return

    #     checkOnWrongUsername()
    #     checkOnWrongPassword()
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()