import json
import httplib2
import pprint
class LoginBusiness:
    FACEBOOK_CLIENT_ID = ''
    FACEBOOK_CLIENT_SECRET = ''
    LONG_TERM_ACCESS_TOKEN= ''
    USER_EMAIL = ''
    USER_NAME = ''
    USER_ID = ''
    USER_PHOTO = ''
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
            facebookSecrets = open('fb_secrets.json','r').read()
            self.setFacebookClientId(json.loads(facebookSecrets)['web']['client_id'])
            self.setFacebookClientSecret(json.loads(facebookSecrets)['web']['client_secret'])
            return True
        except FileNotFoundError:
            return False

    def getLongTermAccessToken(self, app_id,app_secret,access_token):
        url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id, app_secret, access_token)
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        self.setLongTermAccessToken(json.loads(content.decode('utf-8'))['access_token'])
        return True
    
    def getFacebookUserInfos(self, token):
        url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        data = json.loads(content)
        self.setUserEmail(data['email'])
        self.setUserName(data['name'])
        self.setUserId(data['id'])
        return True
    
    def getUserProfilePhoto(self,token):
        url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redirect=0&height=200&width=200' % token
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        data = json.loads(content)
        self.setProfilePhoto(data['data']['url'])
        return True

    def setFacebookClientId(self,client_id):
        self.FACEBOOK_CLIENT_ID = client_id

    def setFacebookClientSecret(self,client_secret):
        self.FACEBOOK_CLIENT_SECRET = client_secret

    def getFacebookClientId(self):
        return self.FACEBOOK_CLIENT_ID

    def getFacebookClientSecret(self):
        return self.FACEBOOK_CLIENT_SECRET
    
    def setLongTermAccessToken(self, longTermAccessToken):
        self.LONG_TERM_ACCESS_TOKEN = longTermAccessToken
    
    def getLongTermAccessTokenFromFacebook(self):
        return self.LONG_TERM_ACCESS_TOKEN
    
    def setUserEmail(self, userEmail):
        self.USER_EMAIL = userEmail

    def setUserName(self, username):
        self.USER_NAME = username
    
    def setUserId(self, id):
        self.USER_ID = id

    def getUserEmail(self):
        return self.USER_EMAIL
        
    def getUserName(self):
        return self.USER_NAME
    
    def getUserId(self):
        return self.USER_ID
    
    def setProfilePhoto(self, profilePhotoAddress):
        self.USER_PHOTO = profilePhotoAddress

    def getProfilePhoto(self):
        return self.USER_PHOTO