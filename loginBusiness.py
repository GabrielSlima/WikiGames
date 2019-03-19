class LoginBusiness:
    FACEBOOK_CLIENT_ID = ''
    FACEBOOK_CLIENT_SECRETS = ''

    def validateUserSession(self, tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
        if tokenSessionAfterGetRequest == tokenSessionAfterPostRequest:
            return True
        else:
            return False

    def checkIfUserWasAlreadyLogged(self,tokenSessionAfterGetRequest):
        if tokenSessionAfterGetRequest is not None:
            return True
        else:
            return False

    def checkIfFacebookClientSecretsExists(self):
        try:
            facebookSecrets = open('fb_ecrets.json','r').read()
        except FileNotFoundError:
            return False

    def setFacebookClientId(self,client_id):
        self.FACEBOOK_CLIENT_ID = client_id

    def setFacebookClientSecret(self,client_secret):
        self.FACEBOOK_CLIENT_SECRETS = client_secret()