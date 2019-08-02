import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = ('ca01d53b89a120406e5cc40fb64905e3')
    SECRET_KEY = ('kamikaze')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    pass 
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/watchlist_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}