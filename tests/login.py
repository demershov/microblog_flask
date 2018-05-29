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

def checkOnWrongPassword():
    time.sleep(3)
    try:
        bases.FindElement(xpaths.getLoginWrongPasswordMessageXPath())
    except exceptions.NoSuchElementException:
        assert False, "Password is correct, but it shouldn't be"

    assert (bases.driver.current_url == bases.domain + "/login"), "Authentication successfully completed, but it shouldn't be"     

class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver

    # Casual login
    def testCasualLogIn(self):
        bases.Login(bases.username, bases.password)
        # assert (bases.CheckIfLoggedIn()), "Authentication failed"
        if not bases.CheckIfLoggedIn():
                bases.CheckWhyAuthFailed()

    # Negative tests
    # Login with wrong pass
    def testWrongPassLogin(self):
        bases.Login(bases.username, "123" + bases.password + "123")
        checkOnWrongPassword()
    
    # Login with non-existent user
    def testNonExistentUserLogin(self):
        bases.Login("asdsad", "123" + "qwerty1")
        checkOnWrongUsername()
    
    # Login with non-existent user with long username
    def testNonExistentUserLongLogin(self):
        bases.Login("asdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsad", "123" + "qwerty1")
        checkOnWrongUsername()
    
    # Login with non-existent user with long passw
    def testNonExistentUserLongPass(self):
        bases.Login("asdasdasd", "123" + "qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1qwerty1")
        checkOnWrongPassword()
    
    # Смысла это тестить нет, ибо на странице логина поля должны быть 100% заполнены для отправки запроса.
    # Класс required у поля для ввода не пропустит пустое значение
    # Blank password field
    # def testBlankPassField(self):
    #     elem = GoToLoginPage()
        
    #     try:
    #         elem = FindElement(xpaths.getLoginInputXPath())
    #         elem.send_keys(username)
    #     except exceptions.NoSuchElementException:
    #         assert False, "Login input element does not found"
    #         return

    #     try:
    #         elem = FindElement(xpaths.getLoginButtonXPath())
    #         elem.click()
    #     except exceptions.NoSuchElementException:
    #         assert False, "Login button does not found"
    #         return
        
    #     checkOnWrongPassword()
    
    # Аналогично
    # Login with blank usernamefield
    # def testBlankeFields(self):
    #     elem = GoToLoginPage()

    #     try:
    #         elem = FindElement(xpaths.getLoginButtonXPath())
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