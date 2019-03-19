import loginBusiness
import uuid
import unittest

class loginBusinessTests(unittest.TestCase):
    requests = ['GET', 'POST']
    tokenSessionAfterGetRequest = ''
    loginBusinessClass = loginBusiness()
    def tokenValidationShouldBeTrue(self):
        tokenSessionAfterPostRequest = ''
        for request in self.requests:
            if request == 'POST':
                if loginBusinessClass.validateUserSession(tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
                    print('TEST 1 SUCCESS: tokenValidationShouldBeTrue')
                else:
                    print('TEST 1 FAILED: tokenValidationShouldBeTrue')
            tokenSessionAfterGetRequest = str(uuid.uuid4())
            tokenSessionAfterPostRequest = tokenSessionAfterGetRequest

    def tokenValidationShouldBeFalse(self):
        tokenSessionAfterPostRequest = ''
        for request in self.requests:
            if request == 'POST':
                tokenSessionAfterPostRequest = str(uuid.uuid4())
            tokenSessionAfterGetRequest = str(uuid.uuid4())
        if not loginBusiness.validateUserSession(tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
            print('TEST 2 SUCCESS: tokenValidationShouldBeFalse')
        else:
            print('TEST 2 FAILED: tokenValidationShouldBeFalse')

    def checkIfUserWasAlreadyLogged(self):
        tokenSessionAfterGetRequest = str(uuid.uuid4())
        if loginBusiness.checkIfUserWasAlreadyLogged(tokenSessionAfterGetRequest):
            print('TEST 3 SUCCESS: checkIfUserWasAlreadyLogged')
        else:
            print('TEST 3 FAILED: checkIfUserWasAlreadyLogged')
       
    def shouldThrowExceptionWhenHasNoClientSecretsFile(self):
        if not loginBusiness.checkIfFacebookClientSecretsExists():
            print('TEST 4 SUCCESS: shouldThrowExceptionWhenHasNoClientSecretsFile')
        else:
            print('TEST 4 FAILED: shouldThrowExceptionWhenHasNoClientSecretsFile')

tests = loginBusinessTests()
tests.tokenValidationShouldBeTrue()
tests.tokenValidationShouldBeFalse()
tests.checkIfUserWasAlreadyLogged()
tests.shouldThrowExceptionWhenHasNoClientSecretsFile()