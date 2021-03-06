'''Configuration classes module'''

import os

class Config:

    '''
    General configuration parent class
    '''

    SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass


class DevConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


CONFIG_OPTIONS = {
    'development': DevConfig,
    'production': ProdConfig
}
