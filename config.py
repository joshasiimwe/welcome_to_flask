import os

class BaseConfig(object):
	DEBUG = False
	SECRTE_KEY = '\xcf)\xdb=+\x10\xeb\xe6U\xf2\x89\xf1>s\x19\xa7X\x1a\xc2\x99\x97\xf6\xc5\x7f'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False


