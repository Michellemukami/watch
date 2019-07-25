import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('52aa730a904ebb3fec8e777c735c94a1')
    SECRET_KEY = os.environ.get('52aa730a')


class ProdConfig(Config):
    pass 


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
