import os
from dotenv import load_dotenv
load_dotenv()




class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://iiljmuorilputx:f604b9247d0b76c3d418eafdc3cc692961cf41572bf2b69c1b66a820b077774e@ec2-3-217-113-25.compute-1.amazonaws.com:5432/dep5de82na2p6d'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://iiljmuorilputx:f604b9247d0b76c3d418eafdc3cc692961cf41572bf2b69c1b66a820b077774e@ec2-3-217-113-25.compute-1.amazonaws.com:5432/dep5de82na2p6d'

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

# 'postgresql+psycopg2://diana:access@localhost/pitchesapp'