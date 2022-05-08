# class Config:
#      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:access@localhost/watchlist'
import os

class Config:
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:access@localhost/watchlist'


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
