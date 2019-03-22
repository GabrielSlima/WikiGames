from engine import engine
from model import Game, User, Category
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind = engine))

def deleteUser(user_id):
    try:
        user = session.query(User).filter_by(id = user_id).one()
        session.delete(user)
        session.commit()
    except Exception as err:
        return err    

def updateUser(user_id, user_name, user_email, user_picture):
    try:
        newUser = session.query(User).filter_by(id = user_id).one()
        newUser.name = user_name
        newUser.email = user_email
        newUser.picture = user_picture
        session.add(newUser)
        session.commit()
    except Exception as err:
        return err

def getUserId(user_email):
    try:
        user = session.query(User).filter_by(email = user_email).one()
        return user.id
    except:
        return None

def getUser(user_id):
    try:
        user = session.query(User).filter_by(id = user_id).one()
        return user
    except:
        return None

def lisUsers():
    try:
        users = session.query(User).all()
        return users
    except:
        return None

def createUser(user_name, user_email, user_picture):
    try:
        user = User(name = user_name, email = user_email, picture = user_picture)
        session.add(user)
        session.commit()
        user = session.query(User).filter_by(email = user_email).one()
        return user.id
    except:
        return None
        
def getCategory(category_id):
    try:
        category = session.query(Category).filter_by(id = category_id).one()
        return category
    except:
        return None

def deleteCategory(category_id):
    try:
        category = session.query(Category).filter_by(id = category_id).one()
        session.delete(category)
        session.commit()
    except Exception as err:
        return err
        
def updateCategory(category_id, category_title, category_descr, category_user_id):
    try:
        newCategory = session.query(Category).filter_by(id = category_id).one()
        newCategory.title = category_title
        newCategory.description = category_descr
        newCategory.user_id = category_user_id
        session.add(newCategory)
        session.commit()
    except Exception as err:
        return err

def listCategories():
    try:
        categories = session.query(Category).all()
        return categories
    except:
        return None

def createCategory(category_title, category_descr, category_user_id):
    try:
        category = Category(title = category_title, description=category_descr, user_id = category_user_id)
        session.add(category)
        session.commit()
    except Exception as err:
        return err

def getGamesByCategory(id_category):
    try:
        games = session.query(Game).filter_by(category_id = id_category)
        return games
    except:
        return None

def getGame(game_id):
    try:
        game = session.query(Game).filter_by(id = game_id).one()
        return game
    except:
        return None

def getLastAddedGames():
    try:
        games = session.query(Game, Category).filter(Game.category_id == Category.id).limit(10).all()
        return games
    except:
        return None

def listGames():
    try:
        games = session.query(Game).all()
        return games
    except:
        return None

def createGame(game_title, game_short_descr, game_long_descr,game_category_id,game_user_id):
    try:
        game = Game(title = game_title, short_description = game_short_descr, long_description = game_long_descr, category_id = game_category_id, user_id = game_user_id)
        session.add(game)
        session.commit()    
    except Exception as err:
        return err

def editGame(game_id, game_title, game_short_descr, game_long_descr,game_category_id,game_user_id):
    try:
        newGame = session.query(Game).filter_by(id=game_id).one()
        newGame.title = game_title
        newGame.short_description = game_short_descr
        newGame.long_description = game_long_descr
        newGame.category_id = game_category_id
        newGame.user_id = game_user_id
        session.add(newGame)
        session.commit()
        newGame = session.query(Game).filter_by(id = game_id).one()
        return newGame
    except:
        return None

def deleteGame(gameId):
    try:
        game = session.query(Game).filter_by(id = gameId).one()
        session.delete(game)
        session.commit()
    except Exception as err:
        return err