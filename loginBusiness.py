import json
import httplib2
import pprint
import operations
import requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError


class LoginBusiness:
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    LONG_TERM_ACCESS_TOKEN = ''
    PROVIDER = ''
    USER_EMAIL = ''
    USER_NAME = ''
    USER_ID = ''
    USER_PHOTO = ''
    CREDENTIALS_DATA = ''
    CONTENT_RETURNED_FROM_CREDENTIALS_TOKEN_VALIDATION = ''

    def validateUserSession(
            self,
            tokenSessionAfterGetRequest,
            tokenSessionAfterPostRequest):
        if tokenSessionAfterGetRequest == tokenSessionAfterPostRequest:
            return True
        return False

    def checkIfUserWasAlreadyLogged(self, tokenSessionAfterGetRequest):
        if tokenSessionAfterGetRequest is not None:
            return True
        return False

    def checkIfFacebookClientSecretsExists(
            self,
            fbSecretsFileNameWithExtension):
        try:
            facebookSecrets = open(fbSecretsFileNameWithExtension, 'r').read()
            try:
                self.setClientId(json.loads(
                    facebookSecrets)['web']['client_id'])
                self.setClientSecret(json.loads(
                    facebookSecrets)['web']['client_secret'])
                return True
            except KeyError:
                return False
        except FileNotFoundError:
            return False

    def getLongTermAccessToken(self, app_id, app_secret, access_token):
        url = ('https://graph.facebook.com/oauth/access_token?grant_type='
        'fb_exchange_token&client_id=%s&client_secret=%s&'
        'fb_exchange_token=%s' % (app_id, app_secret, access_token))
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        self.setLongTermAccessToken(json.loads(
            content.decode('utf-8'))['access_token'])
        return True

    def getFacebookUserInfos(self, token):
        url = ('https://graph.facebook.com/v2.8/me?access_'
        'token=%s&fields=name,id,email' % token)
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        data = json.loads(content.decode('utf-8'))
        self.setProvider('facebook')
        self.setUserEmail(data['email'])
        self.setUserName(data['name'])
        self.setUserId(data['id'])
        return True

    def getUserProfilePhoto(self, token):
        url = ('https://graph.facebook.com/v2.8/me/picture?'
        'access_token=%s&redirect=0&height=200&width=200' % token)
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        data = json.loads(content.decode('utf-8'))
        self.setProfilePhoto(data['data']['url'])
        return True

    def getLocalUserId(self, login_session):
        id = operations.getUserId(login_session['email'])
        if id is None:
            id = operations.createUser(
                login_session['username'],
                login_session['email'],
                login_session['picture'])
        self.setLocalUserId(id)
        return id

    def readGoogleSecretsData(self, googleSecretsFileNameWithExtension):
        try:
            googleSecrets = open(
                googleSecretsFileNameWithExtension, 'r').read()
            try:
                self.setClientId(json.loads(googleSecrets)['web']['client_id'])
                return True
            except KeyError:
                return False
        except FileNotFoundError:
            return False

    def excangeCodeForCredentialObject(
            self,
            code,
            clientSecretsFileWithExtension):
        try:
            oauth_flow = flow_from_clientsecrets(
                clientSecretsFileWithExtension, scope='')
            oauth_flow.redirect_uri = 'postmessage'
            credentials = oauth_flow.step2_exchange(code)
            self.setCredentialsData(credentials)
            return True
        except FlowExchangeError as error:
            print(error)
            return False

    def validateGoogleToken(self, accessToken):
        url = ('https://www.googleapis.com/oauth2/v1/'
        'tokeninfo?access_token=%s' % accessToken)
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False
        content = json.loads(content.decode('utf-8'))
        if content.get('error') is not None:
            return False
        self.setContentReturnedFromGoogleTokenValidation(content)
        return True

    def isTheDataIsFromTheSameUserThatGaranteedAccess(
            self,
            userIdThatGaranteedAccessOnLogin,
            userIdFromAcessDataResponse):
        if userIdThatGaranteedAccessOnLogin != userIdFromAcessDataResponse:
            return False
        return True

    def theResponseDataShouldBeDirectedToAnotherApp(
            self,
            appIdFromCredentialsFile,
            appIdFromAcessDataResponse):
        if appIdFromCredentialsFile != appIdFromAcessDataResponse:
            return False
        return True

    def getUserInformationFromGoogleApi(self, accessToken):
        url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        params = {'access_token': accessToken, 'alt': 'json'}
        content = requests.get(url, params=params)
        content = content.json()
        self.setProvider('google')
        self.setUserName(content['name'])
        self.setUserEmail(content['email'])
        self.setProfilePhoto(content['picture'])
        return True

    def setClientId(self, client_id):
        self.CLIENT_ID = client_id

    def setClientSecret(self, client_secret):
        self.CLIENT_SECRET = client_secret

    def getClientId(self):
        return self.CLIENT_ID

    def getClientSecret(self):
        return self.CLIENT_SECRET

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

    def setLocalUserId(self, localUserId):
        self.LOCAL_USER_ID = localUserId

    def setCredentialsData(self, credentialsData):
        self.CREDENTIALS_DATA = credentialsData

    def getCredentialsData(self):
        return self.CREDENTIALS_DATA

    def setContentReturnedFromGoogleTokenValidation(self, contentData):
        self.CONTENT_RETURNED_FROM_CREDENTIALS_TOKEN_VALIDATION = contentData

    def getDataFromTokenValidation(self):
        return self.CONTENT_RETURNED_FROM_CREDENTIALS_TOKEN_VALIDATION

    def setProvider(self, providerName):
        self.PROVIDER = providerName

    def getProvider(self):
        return self.PROVIDER
