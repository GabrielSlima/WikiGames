import loginBusiness
import uuid
import httplib2
from tempfile import gettempdir
import os
import json
class loginBusinessTests():
    requests = ['GET', 'POST']
    tokenSessionAfterGetRequest = ''

    def tokenValidationShouldBeTrue(self):
        tokenSessionAfterPostRequest = ''
        for request in self.requests:
            if request == 'POST':
                if loginBusiness.LoginBusiness().validateUserSession(tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
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
        if not loginBusiness.LoginBusiness().validateUserSession(tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
            print('TEST 2 SUCCESS: tokenValidationShouldBeFalse')
        else:
            print('TEST 2 FAILED: tokenValidationShouldBeFalse')

    def checkIfUserWasAlreadyLogged(self):
        tokenSessionAfterGetRequest = str(uuid.uuid4())
        if loginBusiness.LoginBusiness().checkIfUserWasAlreadyLogged(tokenSessionAfterGetRequest):
            print('TEST 3 SUCCESS: checkIfUserWasAlreadyLogged')
        else:
            print('TEST 3 FAILED: checkIfUserWasAlreadyLogged')
       
    def shouldThrowExceptionWhenHasNoClientSecretsFile(self):
        if not loginBusiness.LoginBusiness().checkIfFacebookClientSecretsExists('fbSecretsFileNameWithExtension.json'):
            print('TEST 4 SUCCESS: shouldThrowExceptionWhenHasNoClientSecretsFile')
        else:
            print('TEST 4 FAILED: shouldThrowExceptionWhenHasNoClientSecretsFile')

    def shouldThrowExceptionWhenRequestDataIsIncorrect(self):
        app_id = 'id'
        app_secret = 'secret'
        access_token = 'token'
        if not loginBusiness.LoginBusiness().getLongTermAccessToken(app_id,app_secret,access_token):
            print('TEST 5 SUCCESS: shouldThrowExceptionWhenRequestDataIsIncorrect')
        else:
            print('TEST 5 FAILED: shouldThrowExceptionWhenRequestDataIsIncorrect')


    def shouldThrowExceptionWhenLongTermTokenIsInvalid(self):
        token = str(uuid.uuid4)
        if not loginBusiness.LoginBusiness().getFacebookUserInfos(token):
            print('TEST 6 SUCCESS: shouldThrowExceptionWhenLongTermTokenIsInvalid')
        else:
            print('TEST 6 FAILED: shouldThrowExceptionWhenLongTermTokenIsInvalid')

    def shouldThrowExceptionsWhenLongTermTokenIsInvalidForRetrievePhoto(self):
        token = str(uuid.uuid4)
        if not loginBusiness.LoginBusiness().getUserProfilePhoto(token):
            print('TEST 7 SUCCESS: shouldThrowExceptionsWhenLongTermTokenIsInvalidForRetrievePhoto')
        else:
            print('TEST 7 FAILED: shouldThrowExceptionsWhenLongTermTokenIsInvalidForRetrievePhoto')

    def shouldThrowExceptionIfClientSecretsFileDoesNotExists(self):
        if not loginBusiness.LoginBusiness().readGoogleSecretsData('googleSecretsFileNameWithExtension.json'):
            print('TEST 8 SUCCESS: shouldThrowExceptionIfClientSecretsFileDoesNotExists')
        else:
            print('TEST 8 FAILED: shouldThrowExceptionIfClientSecretsFileDoesNotExists')

    def shouldThrowExceptionWhenTheClientIdIsNotPresent(self):
        absoluteTempFilePath = os.path.join(gettempdir(),'googleSecretsFile.json')
        fakeData = {"web":{"clientid":"someid"}}
        tmp = open(absoluteTempFilePath, 'w+')
        tmp.write(json.dumps(fakeData))
        tmp.close()
        if not loginBusiness.LoginBusiness().readGoogleSecretsData(absoluteTempFilePath):
            print('TEST 9 SUCCESS: shouldThrowExceptionWhenTheClientIdIsNotPresent')
        else:
            print('TEST 9 FAILED: shouldThrowExceptionWhenTheClientIdIsNotPresent')

    def shouldThrowExceptionWhenTheCodeIsInvalid(self):
        fakeToken = str(uuid.uuid4)
        if not loginBusiness.LoginBusiness().excangeCodeForCredentialObject(fakeToken,'gplus_client_secret.json'):
            print('TEST 10 SUCCESS: shouldThrowExceptionWhenTheCodeIsInvalid')
        else:
            print('TEST 10 FAILED: shouldThrowExceptionWhenTheCodeIsInvalid')

tests = loginBusinessTests()
tests.tokenValidationShouldBeTrue()
tests.tokenValidationShouldBeFalse()
tests.checkIfUserWasAlreadyLogged()
tests.shouldThrowExceptionWhenHasNoClientSecretsFile()
tests.shouldThrowExceptionWhenRequestDataIsIncorrect()
tests.shouldThrowExceptionWhenLongTermTokenIsInvalid()
tests.shouldThrowExceptionsWhenLongTermTokenIsInvalidForRetrievePhoto()
tests.shouldThrowExceptionIfClientSecretsFileDoesNotExists()
tests.shouldThrowExceptionWhenTheClientIdIsNotPresent()
tests.shouldThrowExceptionWhenTheCodeIsInvalid()