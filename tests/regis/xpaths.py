def getRegPageXPath():
    return "//*[@id='navbarResponsive']/ul/li[3]/a"

def getRegUsernameFieldXPapth():
    return "//*[@id='username']"

def getEmailFieldXPapth():
    return "//*[@id='email']"


def getPasswordXPapth():
    return "//*[@id='password']"

def getConfirmPasswordXPapth():
    return "//*[@id='password2']"

def getRegButton():
    return "//*[@id='submit']"

def getUsernameErrorMessage():
    return "/html/body/div/form/div[2]/div[3]/div/span/i"

def getEmailErrorMessage():
    return "/html/body/div/form/div[3]/div[3]/div/span/i"

def getPasswordErrorMessage():
    return "/html/body/div/form/div[4]/div[3]/div/span/i"

def getConfirmationPasswordErrorMessage():
    return "/html/body/div/form/div[5]/div[3]/div/span/i"