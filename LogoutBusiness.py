import httplib2


class logoutBusiness:
    def disconnectFromGoogle(self, login_session):
        url = (
            'https://accounts.google.com/o/oauth2/'
            'revoke?token=%s' % login_session['access_token'])
        http = httplib2.Http()
        header, content = http.request(url, 'GET')
        if header['status'] != '200':
            return False

        del login_session['gplus_id']
        del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['local_user_id']
        return True

    def disconnectFromFacebook(self, login_session):
        del login_session['user_id_facebook']
        del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['local_user_id']
        return True
