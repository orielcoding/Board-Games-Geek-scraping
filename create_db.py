from sqlalchemy import create_engine, Column, Integer, ForeignKey, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
import json

with open("BGG_configuration.json", "r") as f:
    config = json.load(f)


def deploy_db():
    """
    The following function use mysql connector to create db with specific name if isn't exist already.

    You need to set in the BGG_configuration.json file the appropriate 'host', 'user', 'password' values
    in the "mysql" dictionary, by your mysql logging information.
    """
    cnx = mysql.connector.connect(
                                host=config["mysql"]["host"],
                                user=config["mysql"]["user"],
                                password=config["mysql"]["password"]
    )
    cursor = cnx.cursor()
    query = f"CREATE DATABASE IF NOT EXISTS {config['alchemy']['db_name']}"
    cursor.execute(query)
    cursor.close()
    cnx.close()

def main():
    deploy_db()

    engine = create_engine(config["alchemy"]['SQLAlchemy_db_connection'], echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()


    class Game(Base):
        __tablename__ = 'game'
        site_id = Column(Integer, primary_key=True, autoincrement=False)
        name = Column(String(60))


    class Type(Base):
        __tablename__ = 'types'
        type_id = Column(Integer, primary_key=True, autoincrement=True)
        type = Column(String(60))


    class Artists(Base):
        __tablename__ = 'artists'
        artist_id = Column(Integer, primary_key=True, autoincrement=True)
        artist_name = Column(String(60))


    class Categories(Base):
        __tablename__ = 'categories'
        category_id = Column(Integer, primary_key=True, autoincrement=True)
        category = Column(String(60))


    class Designers(Base):
        __tablename__ = 'designers'
        designer_id = Column(Integer, primary_key=True, autoincrement=True)
        designer_name = Column(String(60))


    class Mechanics(Base):
        __tablename__ = 'mechanics'
        mechanic_id = Column(Integer, primary_key=True, autoincrement=True)
        mechanic = Column(String(60))


    class Sellers(Base):
        __tablename__ = 'sellers'
        seller_id = Column(Integer, primary_key=True, autoincrement=True)
        seller_name = Column(String(60))


    class GameStats(Base):
        __tablename__ = 'game_stats'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        avg_rating = Column(Float)
        overall_rank = Column(Integer)
        type_rank = Column(Integer)
        n_comments = Column(Integer)
        n_page_views = Column(Integer)
        played_all_times = Column(Integer)
        played_last_month = Column(Integer)
        n_own = Column(Integer)
        n_wishlist = Column(Integer)
        n_ratings = Column(Integer)


    class GeneralInfo(Base):
        __tablename__ = 'general_info'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        type_id = Column(Integer, ForeignKey('types.type_id'), primary_key=True, autoincrement=False)
        min_num_players = Column(Integer)
        max_num_players = Column(Integer)
        weight = Column(Float)
        year_published = Column(Integer)
        min_time_duration = Column(Integer)
        max_time_duration = Column(Integer)
        age_limit = Column(Integer)


    class GameArtists(Base):
        __tablename__ = 'game_artists'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        artist_id = Column(Integer, ForeignKey('artists.artist_id'), primary_key=True, autoincrement=False)


    class GameCategory(Base):
        __tablename__ = 'game_category'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True, autoincrement=False)


    class GameDesingers(Base):
        __tablename__ = 'game_designers'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        designer_id = Column(Integer, ForeignKey('designers.designer_id'), primary_key=True, autoincrement=False)


    class GameMechanics(Base):
        __tablename__ = 'game_mechanics'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        mechanics_id = Column(Integer, ForeignKey('mechanics.mechanic_id'), primary_key=True, autoincrement=False)


    class GameSellers(Base):
        __tablename__ = 'game_sellers'
        game_id = Column(Integer, ForeignKey('game.site_id'), primary_key=True, autoincrement=False)
        seller_id = Column(Integer, ForeignKey('sellers.seller_id'), primary_key=True, autoincrement=False)
        price = Column(Float)


    Base.metadata.create_all(engine)

    session.commit()
    session.close()
