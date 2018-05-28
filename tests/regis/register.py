import unittest
import time
import xpaths
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

domain = 'http://127.0.0.1:5000/'
driver = None

# Data for casual registration
username = "testlogin4"
email = "testemail@email.com"
password = "qwerty1"

def getOrCreateWebdriver():
    global driver
    driver = webdriver.Firefox()
    return driver

def findElement(xpath):
        return driver.find_element_by_xpath(xpath)
        
def GoToRegPage():
        assert "Микроблог" in  driver.title
        try:
            elem = findElement(xpaths.getRegPageXPath())
            elem.click()
        except exceptions.NoSuchElementException:
            assert "Reg page link does not found"
            return
        
        assert (driver.current_url == domain + "register"), "Not the reg page"

        return elem

def checkIfRegIsDone():
    time.sleep(2)
    try:
        elem = findElement(xpaths.getUsernameErrorMessage())
        assert len(elem.text) <= 0, "Username error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass
    try:
        elem = findElement(xpaths.getEmailErrorMessage())
        assert len(elem.text) <= 0, "Email error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass
    
    try:
        elem = findElement(xpaths.getPasswordErrorMessage())
        assert len(elem.text) <= 0, "Password error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass    
    
    try:
        elem = findElement(xpaths.getConfirmationPasswordErrorMessage())
        assert len(elem.text) <= 0, "Password confirmation message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass

    assert (driver.current_url == domain + "login"), "Registration does not complete"

def checkOnUsernameFail():
    time.sleep(2)

    try:
        findElement(xpaths.getUsernameErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Username is ok, but it shouldn't be"
    
    assert (driver.current_url == domain + "register"), "Registration successfully completed, but it shouldn't be"

def checkOnEmailFail():
    time.sleep(2)
    
    try:
        findElement(xpaths.getEmailErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Email is ok, but it shouldn't be"
    
    assert (driver.current_url == domain + "register"), "Registration successfully completed, but it shouldn't be"

def checkOnPasswordFail():
    time.sleep(2)

    try:
        findElement(xpaths.getPasswordErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Password is ok, but it shouldn't be"
    
    assert (driver.current_url == domain + "register"), "Registration successfully completed, but it shouldn't be"

def checkOnConfirmPasswordFail():
    time.sleep(2)

    try:
        findElement(xpaths.getConfirmationPasswordErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Password is ok, but it shouldn't be"
    
    assert (driver.current_url == domain + "register"), "Registration successfully completed, but it shouldn't be"

class SiteTest(unittest.TestCase):

    # Setup
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        global domain
        self.driver.get(domain)

    # Casual reg
    def testCasualReg(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys(username)
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys(email)
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys(password)
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys(password)
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkIfRegIsDone()
    
    # Fail tests
    # Existing user reg
    def testExistingUserReg(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark")
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail.ru")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnUsernameFail()

    # Blank username field reg
    def testBlankUsernameReg(self):
        elem = GoToRegPage()

        # Skipping the username field here
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail.ru")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnUsernameFail()
    
    # Existing email reg
    def testExistingEmailrReg(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark")
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail.ru")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()

    # Invalid email 1
    def testInvalidEmailReg1(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid email 2
    def testInvalidEmailReg2(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid email 3
    def testInvalidEmailReg3(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()

    # Invalid email 4
    def testInvalidEmailReg4(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid email 5 / blank
    def testInvalidEmailReg5(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        # Skipping the email field here
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid password 1 / blank fields
    def testInvalidPassword1(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        # Skipping both password fields here
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnPasswordFail()
        checkOnConfirmPasswordFail()
    
    # Invalid password 2 / blank password field
    def testInvalidPassword2(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty123")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnPasswordFail()
        checkOnConfirmPasswordFail()

    # Invalid password 3 / blank confirmation password field
    def testInvalidPassword3(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnConfirmPasswordFail()
        
    # Invalid password 4 / password field does not match confirmation password field
    def testInvalidPassword4(self):
        elem = GoToRegPage()

        try:
            elem = findElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getPasswordXPapth())
            elem.send_keys("qwerty")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getConfirmPasswordXPapth())
            elem.send_keys("qwerty123")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = findElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnConfirmPasswordFail()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()