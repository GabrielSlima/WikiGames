from flask import Flask
from flask import render_template
from flask import request

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
    print(allCategories)
    lastAddedGames = operations.getLastAddedGames()
    print(lastAddedGames)
    return render_template('categories.html', categories=allCategories, items=lastAddedGames)
    # return render_template('publiccategories.html', categories=allCategoriesMock, items=gamesListMock)

@app.route('/category/new', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'POST':
        return 'You added a new category'
    return render_template('addCategory.html')

@app.route('/genre/<string:categoryName>/items')
def showCatalogItems(categoryName):
    return render_template('catalog.html', category=categoryName, items = gamesListMock )
    # return render_template('publiccatalog.html', items = gamesListMock )

@app.route('/genre/<string:genreName>/<int:itemId>')
def showCatalogItem(genreName, itemId):
    return render_template('showItem.html', game = gamemock)
    # return render_template('publicShowItem.html', game = gamemock)
    
@app.route('/catalog/<string:catalog_name>/item/new', methods=['GET', 'POST'])
def addCatalogItem(catalog_name):
    if request.method == 'POST':
        return 'Voce acaba de inserir um novo game'
    return render_template('addCatalogItem.html', category=catalog_name)
@app.route('/catalog/<int:itemId>/edit', methods=['GET', 'POST'])
def editCatalogItem(itemId):
    if request.method == 'POST':
        return 'Voce editou o item.'
    if request.method == 'GET':
        return render_template('editCatalogItem.html', item=gamemock, categories=allCategoriesMock)

@app.route('/catalog/<int:itemId>/delete', methods=['GET', 'POST'])
def deleteCatalogItem(itemId):
    print(request.method)
    if request.method == 'POST':
        return 'Voce deletou o item.'
    if request.method == 'GET':
        return render_template('deleteCatalogItem.html', game=gamemock)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)