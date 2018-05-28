def getLoginPageXPath():
    return "//*[@id='navbarResponsive']/ul/li[2]/a"

def getLoginInputXPath():
    return "//*[@id='username']"

def getLoginPassXPath():
    return "//*[@id='password']"

def getLoginButtonXPath():
    return "//*[@id='submit']"

def getWrongUsernameMessageXPath():
    return "/html/body/div/form/div[2]/div[2]/div/span"

def getWrongPasswordMessageXPath():
    return "/html/body/div/form/div[3]/div[2]/div/span"

def getNavbarUsernameXPath():
    return "//*[@id='navbarResponsive']/ul/li[3]/a"    