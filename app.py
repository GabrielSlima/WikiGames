from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask import make_response
import json
import operations

app = Flask(__name__)
gamemock = {'id': 1,'name': 'Doom', 'description': 'Doom is a first-person shooter video game developed by id Software and published by Bethesda Softworks. A reboot of the Doom franchise, it is the fourth title in the main series and the first major installment since Doom 3 in 2004.'}
allCategoriesMock = [
    {'id': 1 ,'title': "80's fps", 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'},
    {'id': 2 ,'title': "80's adventure", 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'},
    {'id': 2 ,'title': "80's music", 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'}
]

gamesListMock = [
    {
        'id':1, 
'title': 'Dom',
'category':'80s fps', 
'description': 'Doom is a first-person shooter video game developed by id Software and published by Bethesda Softworks. A reboot of the Doom franchise, it is the fourth title in the main series and the first major installment since Doom 3 in 2004.'
},
{
    'id':2,
    'title': 'Counter Strike',
    'category':'80s fps',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'
    },
{
    'id':3,
    'title': '007',
    'category':'80s fps',
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'
    }]
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return 'Você acabou de deslogar do nosso app'
    return render_template('logout.html')

@app.route('/')
@app.route('/categories')
def showCategories():
    allCategories = operations.listCategories()
    lastAddedGamesAndYourCategories = operations.getLastAddedGames()
    return render_template('categories.html', categories=allCategories, items=lastAddedGamesAndYourCategories)
    # return render_template('publiccategories.html', categories=allCategoriesMock, items=gamesListMock)

@app.route('/category/new', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'POST':
        categoryTitle = request.form['title']
        categoryDescription = request.form['description']
        print(categoryTitle)
        print(categoryDescription)
        if categoryDescription == "":
            categoryDescription = '-'
        if categoryTitle != "":
            operations.createCategory(categoryTitle, categoryDescription, '1')
            # flash('%s was added to your repository!' % categoryTitle)
        return redirect('/')
    return render_template('addCategory.html')

@app.route('/genre/<int:categoryId>/items')
def showCatalogItems(categoryId):
    try:
        foundedCategory = operations.getCategory(categoryId)
        gameList = operations.getGamesByCategory(categoryId)
        return render_template('catalog.html', category = foundedCategory, items = gameList )
    except Exception:
        response = make_response(json.dumps('There is no items related with this category id...'),404)
        response.headers['Content-Type'] = 'application/json'
        return response
    # return render_template('publiccatalog.html', items = gamesListMock )

@app.route('/genre/<string:genreName>/<int:itemId>')
def showCatalogItem(genreName, itemId):
    try:
        foundedGame = operations.getGame(itemId)
        return render_template('showItem.html', game = foundedGame)
    except Exception:
        response = make_response(json.dumps('There is no game related to this game id...'),404)
        response.headers['Content-Type'] = 'application/json'
        return response
    # return render_template('publicShowItem.html', game = gamemock)
    
@app.route('/catalog/<int:catalog_id>/item/new', methods=['GET', 'POST'])
def addCatalogItem(catalog_id):
    try: 
        catalog = operations.getCategory(catalog_id)
    except Exception:
        response = make_response(json.dumps('There is no category related with this category id...'),404)
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
            operations.createGame(gameTitle,gameShortDescription,gameLongDescription,catalog_id, '1')
            return redirect(url_for('showCatalogItems', categoryId = catalog_id))
    return render_template('addCatalogItem.html', category=catalog)

@app.route('/catalog/<int:itemId>/edit', methods=['GET', 'POST'])
def editCatalogItem(itemId):
    try:
        game = operations.getGame(itemId)
        allCategories = operations.listCategories()
    except Exception:
        response = make_response(json.dumps('There is no item related with this item id...'),404)
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
            newGame = operations.editGame(itemId, gameTitle, gameShortDescription, gameLongDescription, gameCategory, '1')
            print(newGame.category_id)
            return redirect(url_for('showCatalogItems', categoryId = newGame.category_id))
    if request.method == 'GET':
        return render_template('editCatalogItem.html', item=game, categories=allCategories)

@app.route('/catalog/<int:itemId>/delete', methods=['GET', 'POST'])
def deleteCatalogItem(itemId):
    try:
        game = operations.getGame(itemId)
        gameCategory = game.category_id
    except Exception:
        response = make_response(json.dumps('This game id does not exists on our reposiotry.'), 404)
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST':
        try:
            operations.deleteGame(itemId)
            # flash
            return redirect(url_for('showCatalogItems', categoryId=gameCategory))
        except:
            response = make_response(json.dumps('An error has occured, please contact the administrators or try agin later...'), 500)
            response.headers['Content-Type'] = 'application/json'
            return response
    if request.method == 'GET':
        return render_template('deleteCatalogItem.html', game=game)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)