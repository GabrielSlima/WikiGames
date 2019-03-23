from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask import make_response
from flask import session as login_session
from flask import jsonify

import json
import uuid

import operations
import loginBusiness
import LogoutBusiness
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in login_session:
        return redirect('/')
    if request.method == "POST":
        loginbusiness = loginBusiness.LoginBusiness()
        print('LOGINFO: VALIDATING TOKEN SESSION...')
        if not loginbusiness.validateUserSession(
                login_session['user_token'], request.args.get('state')):
            response = make_response(json.dumps(
                'Occured an error, please, try log in again!'), 500)
            response.headers['Content-Type'] = 'application/json'
            return response
        print('LOGINFO: CHECKING IF THE USER WAS ALREADY LOGGED...')
        if loginBusiness.LoginBusiness().checkIfUserWasAlreadyLogged(
                login_session.get('access_token')):
            response = make_response(json.dumps(
                'The user was already logged...'), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
        print('LOGINFO: CHECKING THE PLATFORM...')
        if request.args.get('platform') == 'facebook':
            print('LOGINFO: DONE! PLATFORM=%s' %request.args.get('platform'))
            facebookAccessToken = request.data.decode('utf-8')
            print('LOGINFO: CHECKING CLIENT SECRETS...')
            if not loginbusiness.checkIfFacebookClientSecretsExists(
                    'fb_secrets.json'):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: GETTING LONGTERM ACCESSTOKEN...')
            if not loginbusiness.getLongTermAccessToken(
                    loginbusiness.getClientId(),
                    loginbusiness.getClientSecret(),
                    facebookAccessToken):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: BUILDING A SESSION FOR THE USER...')
            facebookLongTermAccessToken = \
                loginbusiness.getLongTermAccessTokenFromFacebook()
            print('LOGINFO: DONE...')
            login_session['access_token'] = facebookLongTermAccessToken
            print('LOGINFO: GETTING USERINFOS...')
            loginbusiness.getFacebookUserInfos(login_session['access_token'])
            print('LOGINFO: DONE...')
            login_session['provider'] = loginbusiness.getProvider()
            login_session['user_id_facebook'] = loginbusiness.getUserId()
            login_session['username'] = loginbusiness.getUserName()
            login_session['email'] = loginbusiness.getUserEmail()
            print('LOGINFO: GETTING USER PHOTO...')
            if not loginbusiness.getUserProfilePhoto(
                    login_session['access_token']):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            login_session['picture'] = loginbusiness.getProfilePhoto()
            login_session['local_user_id'] = \
                loginbusiness.getLocalUserId(login_session)
            print('LOGINFO: DONE...')
        if request.args.get('platform') == 'google':
            print('LOGINFO: DONE! PLATFORM=%s' % request.args.get('platform'))
            if not loginbusiness.readGoogleSecretsData(
                    'gplus_client_secret.json'):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: BUILDING A CREDENTIAL OBJECT...')
            if not loginbusiness.excangeCodeForCredentialObject(
                    request.data,
                    'gplus_client_secret.json'):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: VALIDATING TOKEN...')
            if not loginbusiness.validateGoogleToken(
                    loginbusiness.getCredentialsData().access_token):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: VALIDATING USER...')
            if not loginbusiness.isTheDataIsFromTheSameUserThatGaranteedAccess(
                        loginbusiness.getCredentialsData().id_token['sub'],
                        loginbusiness.getDataFromTokenValidation()['user_id']):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: VALIDATING APP...')
            if not loginbusiness.theResponseDataShouldBeDirectedToAnotherApp(
                    loginbusiness.getDataFromTokenValidation()['issued_to'],
                    loginbusiness.getClientId()):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 500)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: CHECKING IF USER WAS ALREADY LOGGED...')
            if loginBusiness.LoginBusiness().checkIfUserWasAlreadyLogged(
                    login_session.get('gplus_id')):
                response = make_response(json.dumps(
                    'The user was already logged...'), 200)
                response.headers['Content-Type'] = 'application/json'
                return response

            login_session['access_token'] = \
                loginbusiness.getCredentialsData().access_token
            login_session['gplus_id'] = \
                loginbusiness.getCredentialsData().id_token['sub']
            print('LOGINFO: GETTING USER INFOS...')
            if not loginbusiness.getUserInformationFromGoogleApi(
                    loginbusiness.getCredentialsData().access_token):
                response = make_response(json.dumps(
                    'Occured an error, please, try log in again!'), 200)
                response.headers['Content-Type'] = 'application/json'
                return response
            print('LOGINFO: BUILDING USER SESSION...')
            login_session['provider'] = loginbusiness.getProvider()
            login_session['username'] = loginbusiness.getUserName()
            login_session['email'] = loginbusiness.getUserEmail()
            login_session['picture'] = loginbusiness.getProfilePhoto()
            login_session['local_user_id'] = loginbusiness.getLocalUserId(
                login_session)
            print('LOGINFO: DONE!')
            flash('Welcome!!!')
        return 'Logged with success!'
    if request.method == "GET":
        state = str(uuid.uuid4())
        login_session['user_token'] = state
        return render_template('login.html', STATE=state)


@app.route('/logout')
def logout():
    if login_session.get('access_token') is None:
        response = make_response(json.dumps(
            'You are not logged to log out!'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    logoutBusiness = LogoutBusiness.logoutBusiness()
    if login_session['provider'] == 'google':
        if not logoutBusiness.disconnectFromGoogle(login_session):
            response = make_response(json.dumps(
                'Occurred an error when trying to logout, please,' +
                ' try to clear you browser cache.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

    if login_session['provider'] == 'facebook':
        logoutBusiness.disconnectFromFacebook(login_session)
    flash('You are not logged in!')
    return redirect('/')


@app.route('/categories/api')
def cateogiesApi():
    allCategories = operations.listCategories()
    return jsonify(Categories=[i.serialize for i in allCategories])


@app.route('/')
@app.route('/categories')
def showCategories():
    allCategories = operations.listCategories()
    lastAddedGamesAndYourCategories = operations.getLastAddedGames()
    if 'username' in login_session:
        return render_template(
            'categories.html',
            categories=allCategories,
            items=lastAddedGamesAndYourCategories
            )
    return render_template(
        'publiccategories.html',
        categories=allCategories,
        items=lastAddedGamesAndYourCategories)


@app.route('/category/new', methods=['GET', 'POST'])
def addCategory():
    if 'username' not in login_session:
        return redirect('/')
    if request.method == 'POST':
        categoryTitle = request.form['title']
        categoryDescription = request.form['description']
        if categoryDescription == "":
            categoryDescription = '-'
        if categoryTitle != "":
            operations.createCategory(
                categoryTitle,
                categoryDescription,
                login_session.get('local_user_id')
                )

        flash('%s was added to your repository!' % categoryTitle)
        return redirect('/')
    return render_template('addCategory.html')


@app.route('/genre/<int:categoryId>/items')
def showCatalogItems(categoryId):
    try:
        foundedCategory = operations.getCategory(categoryId)
        gameList = operations.getGamesByCategory(categoryId)
        if 'username' not in login_session:
            return render_template(
                'publiccatalog.html',
                category=foundedCategory,
                items=gameList
                )
        return render_template(
            'catalog.html',
            category=foundedCategory,
            items=gameList
            )
    except Exception:
        response = make_response(json.dumps(
            'There is no items related with this category id...'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/genre/<string:genreName>/<int:itemId>')
def showCatalogItem(genreName, itemId):
    try:
        foundedGame = operations.getGame(itemId)
        if 'username' not in login_session:
            return render_template(
                'publicShowItem.html',
                game=foundedGame,
                isAuthor=False
                )

        if login_session.get('local_user_id') != foundedGame.user_id:
            return render_template(
                'publicShowItem.html',
                game=foundedGame,
                isLoged=True
                )
        return render_template('showItem.html', game=foundedGame)
    except Exception:
        response = make_response(json.dumps(
            'There is no game related to this game id...'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/catalog/<int:catalog_id>/item/new', methods=['GET', 'POST'])
def addCatalogItem(catalog_id):
    if 'username' not in login_session:
        return redirect('/')
    try:
        catalog = operations.getCategory(catalog_id)
    except Exception:
        response = make_response(json.dumps(
            'There is no category related with this category id...'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST':
        gameTitle = request.form['title']
        gameShortDescription = request.form['sumary']
        gameLongDescription = request.form['description']
        if gameShortDescription == "":
            gameShortDescription = "-"
        if gameLongDescription == "":
            gameLongDescription = "-"
        if gameTitle != "":
            operations.createGame(
                gameTitle,
                gameShortDescription,
                gameLongDescription,
                catalog_id,
                login_session.get('local_user_id')
                )
            flash('New item added!')
            return redirect(url_for('showCatalogItems', categoryId=catalog_id))
    return render_template('addCatalogItem.html', category=catalog)


@app.route('/catalog/<int:itemId>/edit', methods=['GET', 'POST'])
def editCatalogItem(itemId):
    game = operations.getGame(itemId)
    if ('username' not in login_session or
            login_session.get('local_user_id') != game.user_id):
        return redirect('/')
    try:
        allCategories = operations.listCategories()
    except Exception:
        response = make_response(json.dumps(
            'There is no item related with this item id...'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST':
        gameTitle = request.form['title']
        gameShortDescription = request.form['short_description']
        gameLongDescription = request.form['long_description']
        gameCategory = request.form['category']
        if gameShortDescription is None:
            gameShortDescription = '-'
        if gameLongDescription is None:
            gameLongDescription = '-'
        if gameTitle is not None:
            newGame = operations.editGame(
                itemId,
                gameTitle,
                gameShortDescription,
                gameLongDescription,
                gameCategory,
                login_session.get('local_user_id')
                )
            return redirect(url_for(
                'showCatalogItems',
                categoryId=newGame.category_id)
                )
    if request.method == 'GET':
        return render_template(
            'editCatalogItem.html',
            item=game,
            categories=allCategories
            )


@app.route('/catalog/<int:itemId>/delete', methods=['GET', 'POST'])
def deleteCatalogItem(itemId):
    game = operations.getGame(itemId)
    if ('username' not in login_session or
            login_session.get('local_user_id') != game.user_id):
        return redirect('/')
    try:
        gameCategory = game.category_id
    except Exception:
        response = make_response(json.dumps(
            'This game id does not exists on our reposiotry.'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST':
        try:
            operations.deleteGame(itemId)
            # flash
            return redirect(url_for(
                'showCatalogItems',
                categoryId=gameCategory)
                )
        except:
            response = make_response(json.dumps(
                'An error has occured, please contact the administrators or' +
                ' try agin later...'), 500)
            response.headers['Content-Type'] = 'application/json'
            return response
    if request.method == 'GET':
        return render_template('deleteCatalogItem.html', game=game)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
