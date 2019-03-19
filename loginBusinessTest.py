import loginBusiness
import uuid

def tokenValidationShouldBeTrue():
    tokenSessionAfterGetRequest = ''
    tokenSessionAfterPostRequest = ''
    for request in range(2):
        print(request)
        if request == 1:
            if loginBusiness.validateUserSession(tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
                print('TEST 1 SUCCESS: tokenValidationShouldBeTrue')
            else:
                print('TEST 1 FAILED: tokenValidationShouldBeTrue')

        tokenSessionAfterGetRequest = str(uuid.uuid4())
        tokenSessionAfterPostRequest = tokenSessionAfterGetRequest

tokenValidationShouldBeTrue()
