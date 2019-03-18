from engine import engine
from model import Game, User, Category
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind = engine))

def deleteUser(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    session.delete(user)
    session.commit()

def updateUser(user_id, user_name, user_email, user_picture):
    newUser = session.query(User).filter_by(id = user_id).one()
    newUser.name = user_name
    newUser.email = user_email
    newUser.picture = user_picture
    session.add(newUser)
    session.commit()

def getUserId(user_email):
    user = session.query(User).filter_by(email = user_email).one()
    return user.id

def getUser(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user

def lisUsers():
    users = session.query(User).all()
    return users

def createUser(user_name, user_email, user_picture):
    user = User(name = user_name, email = user_email, picture = user_picture)
    session.add(user)
    session.commit()

def getCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    return category

def deleteCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    session.delete(category)
    session.commit()

def updateCategory(category_id, category_title, category_descr, category_user_id):
    newCategory = session.query(Category).filter_by(id = category_id).one()
    newCategory.title = category_title
    newCategory.description = category_descr
    newCategory.user_id = category_user_id
    session.add(newCategory)
    session.commit()
    
def listCategories():
    categories = session.query(Category).all()
    return categories

def createCategory(category_title, category_descr, category_user_id):
    category = Category(title = category_title, description=category_descr, user_id = category_user_id)
    session.add(category)
    session.commit()

def getGamesByCategory(id_category):
    games = session.query(Game).filter_by(category_id = id_category)
    return games

def getGame(game_id):
    game = session.query(Game).filter_by(id = game_id).one()
    return game

def getLastAddedGames():
    games = session.query(Game, Category).filter(Game.category_id == Category.id).limit(10).all()
    return games

def listGames():
    games = session.query(Game).all()
    return games

def createGame(game_title, game_short_descr, game_long_descr,game_category_id,game_user_id):
    game = Game(title = game_title, short_description = game_short_descr, long_description = game_long_descr, category_id = game_category_id, user_id = game_user_id)
    session.add(game)
    session.commit()    

def editGame(game_id, game_title, game_short_descr, game_long_descr,game_category_id,game_user_id):
    newGame = session.query(Game).filter_by(id=game_id).one()
    newGame.title = game_title
    newGame.short_description = game_short_descr
    newGame.long_description = game_long_descr
    newGame.category_id = game_category_id
    newGame.user_id = game_user_id
    session.add(newGame)
    session.commit()

def deleteGame(gameId):
    game = session.query(Game).filter_by(id = gameId).one()
    session.delete(game)
    session.commit()

