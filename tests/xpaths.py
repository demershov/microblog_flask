# Login
def getLoginPageXPath():
    return "//*[@id='navbarResponsive']/ul/li[2]/a"

def getLoginInputXPath(): 
    return "//*[@id='username']"

def getLoginPassXPath():
    return "//*[@id='password']"

def getLoginButtonXPath():
    return "//*[@id='submit']"

def getRegPageXPath():
    return "//*[@id='navbarResponsive']/ul/li[3]/a"

def getLoginWrongUsernameMessageXPath(): 
    return "/html/body/div/form/div[2]/div[2]/div/span"

def getLoginWrongPasswordMessageXPath():
    return "/html/body/div/form/div[3]/div[2]/div/span"

# Reg
def getRegUsernameFieldXPapth():
    return "//*[@id='username']"

def getRegEmailFieldXPapth():
    return "//*[@id='email']"

def getRegPasswordXPapth():
    return "//*[@id='password']"

def getRegConfirmPasswordXPapth():
    return "//*[@id='password2']"

def getRegButton():
    return "//*[@id='submit']"

def getRegUsernameErrorMessage():
    return "/html/body/div/form/div[2]/div[3]/div/span/i"

def getRegEmailErrorMessage():
    return "/html/body/div/form/div[3]/div[3]/div/span/i"

def getRegPasswordErrorMessage():
    return "/html/body/div/form/div[4]/div[3]/div/span/i"

def getRegConfirmationPasswordErrorMessage():
    return "/html/body/div/form/div[5]/div[3]/div/span/i"

# Edit

def getEditUsernameFieldXPath():
    return "//*[@id='username']"

def getEditEmailFieldXPath():
    return "//*[@id='email']"

def getEditAboutFieldXPath():
    return "//*[@id='about_me']"

def getCancelButtonXPath():
    return "//*[@id='edit']/form/div[4]/div/a"

def getSubmitChangesButtonXPath():
    return "//*[@id='submit']"

def getEditLoginErrorMessage():
    return "//*[@id='edit']/form/div[1]/div/span"

def getEditEmailErrorMessage():
    return "//*[@id='edit']/form/div[2]/div/span"

def getEditAboutInfoErrorMessage():
    return "//*[@id='edit']/form/div[3]/div/span"

# Misc

def getUserMenuNavbarDropdownXPath():
    return "//*[@id='navbarResponsive']/ul/li[3]/a"

def getUserProfileLinkXPath():
    return "//*[@id='navbarResponsive']/ul/li[3]/ul/li[1]/a"

def getFirstPostPageXPath():
    return "/html/body/div/div/div/div/div[3]/div[1]/a"

def getPosterProfileLinkFromPostXPath():
    return "/html/body/div/div/div/p[1]/a"

def getEditPageLinkXPath():
    return "/html/body/div/div/div/ul/li[2]/a"

# Unused
def getUsernameXpath():
    return "//*[@id='navbarResponsive']/ul/li[3]/a"