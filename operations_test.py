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
        print(user.id)
        operations.listAspecificUser(user.id)
        print('TEST 7 SUCCESS: shouldListAspecificUser')
    except Exception as err:
        print('TEST 7 FAILED: shouldListAspecificUser')
        print(err)

def shouldEditAuser():
    try:
        user = operations.lisUsers()[len(operations.lisUsers())-1]
        print(user.name)
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

# shouldAddAnewCategory()
shouldListAllCategories()
shouldUpdateCategory()
shouldDeleteAcategory()
# shouldCreateUsers()
shouldListUsers()
shouldListAspecificUser()
shouldEditAuser()
shouldDeleteAuser()