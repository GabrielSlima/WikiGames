from engine import engine
from model import Game, User, Category
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind = engine))

def createUser(user_name, user_email, user_picture):
    user = User(name = user_name, email = user_email, picture = user_picture)
    session.add(user)
    session.commit()

def createCategory(category_title, category_descr, category_user_id):
    category = Category(title = category_title, description=category_descr, user_id = category_user_id)
    session.add(category)
    session.commit()

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
