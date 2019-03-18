import operations
categoriesMock = [
    {'title': "80's fps", 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'},
    {'title': "80's adventure", 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'},
    {'title': "80's music", 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pretium, lorem nec mollis ullamcorper, magna nulla lobortis eros, quis feugiat orci ipsum ac lorem. Sed aliquam nisi at dolor volutpat pharetra. Nam tincidunt sagittis risus. Suspendisse egestas gravida faucibus. Mauris viverra tortor ut semper pretium. In tincidunt tellus sed tincidunt hendrerit. Phasellus sem velit, auctor sed erat in, egestas consectetur nisi. Nunc at porttitor nulla. Integer nec lorem luctus, vestibulum diam eget, mollis elit. In at odio non nisl rhoncus scelerisque. Vivamus at hendrerit mauris, non feugiat metus. Nunc velit leo, consectetur in lorem sit amet, sollicitudin ullamcorper orci. Nam eget fermentum libero. Phasellus viverra nisi lobortis felis sodales, sed faucibus arcu molestie.'}
    ]
usersMock = [
    {'name':'Marlo', 'email':'marlon@email.com', 'picture':'htts://photos.domain.profile/marlo'},
    {'name':'Gerald', 'email':'gerald@email.com', 'picture':'htts://photos.domain.profile/marlo'},
    {'name':'Whindersson Nunes', 'email':'whinderssonnunes@email.com', 'picture':'htts://photos.domain.profile/marlo'}
    ]
gamesMock = [
    {
        'title':'Doom', 
        'short_description':'The Doom franchise is a series of first-person'+ 
    ' shooter video games developed by id Software, and related novels, comics, board games, and film adaptation.', 
        'long_description': 'Doom is considered to be one of the ' + 
    'pioneering first-person shooter games, introducing to IBM-compatible computers features' + 
    ' such as 3D graphics, third-dimension spatiality, networked multiplayer gameplay, and support' + 
    ' for player-created modifications with the Doom WAD format. Since the release of Doom in 1993,' + 
    ' the series has spawned numerous sequels, expansion packs, and a film.Since its debut,' + 
    ' over 10 million copies of games in the Doom series have been sold.',
        'category_id': '000', 
        'user_id':'000'
        },
    {
        'title': 'Counter Strike',
        'short_description':'Counter-Strike is a series of multiplayer' + 
        ' first-person shooter video games, in which teams of terrorists' + 
        ' battle to perpetrate an act of terror and counter-terrorists' + 
        ' try to prevent it. The series began on Windows in 1999' + 
        ' with the first game, Counter-Strike.',
        'long_description': 'Counter-Strike (CS) is a series of multiplayer' + 
        ' first-person shooter video games, in which teams of terrorists' + 
        ' battle to perpetrate an act of terror (bombing, hostage-taking,' + 
        ' assassination) and counter-terrorists try to prevent it' + 
        ' (bomb defusal, hostage rescue). The series began on Windows in' + 
        ' 1999 with the first game, Counter-Strike. It was initially' + 
        ' released as a modification ("mod") for Half-Life and designed' + 
        ' by Minh "Gooseman" Le and Jess "Cliffe" Cliffe before the rights' + 
        ' to the game\'s intellectual property were acquired by' + 
            ' Valve Corporation, the developers of Half-Life.',
            'category_id': '000',
            'user_id':'000'
        },
    {
        'title': 'Zelda',
    'short_description':'The Legend of Zelda is a fantasy action-adventure' + 
    ' video game franchise created by Japanese game designers' + 
    ' Shigeru Miyamoto and Takashi Tezuka. It is primarily developed ' + 
    ' and published by Nintendo, although some portable installments' + 
    ' and re-releases have been outsourced to Capcom, Vanpool, and Grezzo. ',
    'long_description': 'The Legend of Zelda is a fantasy action-adventure' + 
    ' video game franchise created by Japanese game designers' + 
    ' Shigeru Miyamoto and Takashi Tezuka. It is primarily developed ' + 
    ' and published by Nintendo, although some portable installments' + 
    ' and re-releases have been outsourced to Capcom, Vanpool,' + 
    ' and Grezzo. The series gameplay incorporates' + 
    ' action-adventure and elements of action RPG games.',
    'category_id': '000',
    'user_id':'000'}
    ]
def shouldAddAnewCategory():
    try:
        for category in categoriesMock:
            operations.createCategory(category['title'],category['description'], '00000')
        print('TEST 1 SUCCESS: shouldAddAnewCategory')
    except Exception as err:
        print('TEST 1 FAILED: shouldAddAnewCategory')
        print(err)

def shouldListAllCategories():
    try:
        operations.listCategories()
        print('TEST 2 SUCCESS: shouldListAllCategories')
    except Exception as err:
        print('TEST 2 FAILED: shouldListAllCategories')
        print(err)

def shouldUpdateCategory():
    try:
        category = operations.listCategories()[len(operations.listCategories())-1]
        newCategory = categoriesMock[0]
        operations.updateCategory(category.id, newCategory['title'], newCategory['description'], category.user_id)
        print('TEST 3 SUCCESS: shouldUpdateCategory')        
    except Exception as err:
        print('TEST 3 FAILED: shouldUpdateCategory')
        print(err) 
def shouldDeleteAcategory():
    try:
        category = operations.listCategories()[len(operations.listCategories())-1]
        operations.deleteCategory(category.id)
        print('TEST 4 SUCCESS: shouldDeleteAcategory')        
    except Exception as err:
        print('TEST 4 FAILED: shouldDeleteAcategory')
        print(err)
def shouldCreateUsers():
    try:
        for user in usersMock:
            operations.createUser(user['name'], user['email'], user['picture'])
        print('TEST 5 SUCCESS: shouldCreateUsers')
    except Exception as err:
        print('TEST 5 FAILED: shouldCreateUsers')
        print(err)

def shouldListUsers():
    try:
        operations.lisUsers()
        print('TEST 6 SUCCESS: shouldListUsers')
    except Exception as err:
        print('TEST 6 FAILED: shouldListUsers')
        print(err)

def shouldListAspecificUser():
    try:
        user = operations.lisUsers()[len(operations.lisUsers())-1]
        operations.listAspecificUser(user.id)
        print('TEST 7 SUCCESS: shouldListAspecificUser')
    except Exception as err:
        print('TEST 7 FAILED: shouldListAspecificUser')
        print(err)

def shouldEditAuser():
    try:
        user = operations.lisUsers()[len(operations.lisUsers())-1]
        operations.updateUser(user.id, user.name, user.email, user.picture)
        print('TEST 8 SUCCESS: shouldEditAuser')
    except Exception as err:
        print('TEST 8 FAILED: shouldEditAuser')
        print(err)

def shouldDeleteAuser():
    try:
        user = operations.lisUsers()[len(operations.lisUsers())-1]
        operations.deleteUser(user.id)
        print('TEST 9 SUCCESS: shouldDeleteAuser')
    except Exception as err:
        print('TEST 9 FAILED: shouldDeleteAuser')
        print(err)
def shouldCreateGames():
    try:
        user = operations.lisUsers()[len(operations.lisUsers())-1]
        category = operations.listCategories()[len(operations.listCategories())-1]
        for game in gamesMock:
            game['user_id'] = user.id
            game['category_id'] = category.id
        print('TEST 10 SUCCESS: shouldCreateGames')
    except Exception as err:
        print('TEST 10 FAILED: shouldCreateGames')
        print(err)
def shouldListGames():
    try:
        operations.listGames()
        print('TEST 11 SUCCESS: shouldListGames')
    except Exception as err:
        print('TEST 11 FAILED: shouldListGames')
        print(err)
# shouldAddAnewCategory()
shouldListAllCategories()
shouldUpdateCategory()
# shouldDeleteAcategory()
# shouldCreateUsers()
shouldListUsers()
shouldListAspecificUser()
shouldEditAuser()
# shouldDeleteAuser()
shouldCreateGames()
shouldListGames()
shouldListAspecificGame()