import unittest
import time
import random
import xpaths
from baseFuncs import BaseFunc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

# Data for register new user edit here
username = "testlogin" + str(random.randint(1,60))
email = "test" + str(random.randint(1, 60)) + "@email.com"
password = "qwerty"

bases = BaseFunc()

def getOrCreateWebdriver():
    bases.driver = webdriver.Firefox()
    return bases.driver

def checkIfRegIsDone():
    time.sleep(3)
    try:
        elem = bases.FindElement(xpaths.getRegUsernameErrorMessage())
        assert len(elem.text) <= 0, "Username error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass
    
    try:
        elem = bases.FindElement(xpaths.getRegEmailErrorMessage())
        assert len(elem.text) <= 0, "Email error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass
    
    try:
        elem = bases.FindElement(xpaths.getRegPasswordErrorMessage())
        assert len(elem.text) <= 0, "Password error message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass    
    
    try:
        elem = bases.FindElement(xpaths.getRegConfirmationPasswordErrorMessage())
        assert len(elem.text) <= 0, "Password confirmation message appears: " + elem.text
    except exceptions.NoSuchElementException:
        pass

    assert (bases.driver.current_url == bases.domain + "/login"), "Registration does not complete"


def checkOnUsernameFail():
    time.sleep(2)

    try:
        bases.FindElement(xpaths.getRegUsernameErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Username is ok, but it shouldn't be"
    
    assert (bases.driver.current_url == bases.domain + "/register"), "Registration successfully completed, but it shouldn't be"

def checkOnEmailFail():
    time.sleep(2)
    
    try:
        bases.FindElement(xpaths.getRegEmailErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Email is ok, but it shouldn't be"
    
    assert (bases.driver.current_url == bases.domain + "/register"), "Registration successfully completed, but it shouldn't be"

def checkOnPasswordFail():
    time.sleep(2)

    try:
        bases.FindElement(xpaths.getRegPasswordErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Password is ok, but it shouldn't be"
    
    assert (bases.driver.current_url == bases.domain + "/register"), "Registration successfully completed, but it shouldn't be"

def checkOnConfirmPasswordFail():
    time.sleep(2)

    try:
        bases.FindElement(xpaths.getRegConfirmationPasswordErrorMessage())
    except exceptions.NoSuchElementException:
        assert False, "Password is ok, but it shouldn't be"
    
    assert (bases.driver.current_url == bases.domain + "/register"), "Registration successfully completed, but it shouldn't be"

class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = getOrCreateWebdriver()
        self.driver.implicitly_wait(10)
        self.driver.get(bases.domain)
        bases.driver = self.driver

    # Casual reg
    def testCasualReg(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys(username)
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys(email)
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys(password)
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys(password)
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkIfRegIsDone()
    
    # Fail tests
    # Existing user reg
    def testExistingUserReg(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark")
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail.ru")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnUsernameFail()

    # Blank username field reg
    def testBlankUsernameReg(self):
        elem = bases.GoToRegPage()

        # Skipping the username field here
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail.ru")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnUsernameFail()
    
    # Existing email reg
    def testExistingEmailrReg(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark")
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail.ru")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()

    # Invalid email 1
    def testInvalidEmailReg1(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid email 2
    def testInvalidEmailReg2(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid email 3
    def testInvalidEmailReg3(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()

    # Invalid email 4
    def testInvalidEmailReg4(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid email 5 / blank
    def testInvalidEmailReg5(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        # Skipping the email field here
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty1")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnEmailFail()
    
    # Invalid password 1 / blank fields
    def testInvalidPassword1(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        # Skipping both password fields here
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnPasswordFail()
        checkOnConfirmPasswordFail()
    
    # Invalid password 2 / blank password field
    def testInvalidPassword2(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty123")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnPasswordFail()
        checkOnConfirmPasswordFail()

    # Invalid password 3 / blank confirmation password field
    def testInvalidPassword3(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnConfirmPasswordFail()
        
    # Invalid password 4 / password field does not match confirmation password field
    def testInvalidPassword4(self):
        elem = bases.GoToRegPage()

        try:
            elem = bases.FindElement(xpaths.getRegUsernameFieldXPapth())
            elem.send_keys("naark" + str(random.randint(1, 15)))
        except exceptions.NoSuchElementException:
            assert False, "Username input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegEmailFieldXPapth())
            elem.send_keys("wadernik@mail")
        except exceptions.NoSuchElementException:
            assert False, "Email input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegPasswordXPapth())
            elem.send_keys("qwerty")
        except exceptions.NoSuchElementException:
            assert False, "Password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegConfirmPasswordXPapth())
            elem.send_keys("qwerty123")
        except exceptions.NoSuchElementException:
            assert False, "Confirm password input element does not found"
            return
        
        try:
            elem = bases.FindElement(xpaths.getRegButton())
            elem.click()
        except exceptions.NoSuchElementException:
            assert False, "Reg button does not found"
            return

        checkOnConfirmPasswordFail()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()