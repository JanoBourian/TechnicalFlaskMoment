import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()  # take environment variables from .env.

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") 
    MAIL_SERVER = os.environ.get('MAIL_SERVER') 
    MAIL_PORT = int(os.environ.get("MAIL_PORT")) 
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() 
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 
    FLASKY_MAIL_SUBJECT_PREFIX =os.environ.get("FLASKY_MAIL_SUBJECT_PREFIX")  
    FLASKY_MAIL_SENDER = os.environ.get("FLASKY_MAIL_SENDER") 
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN") 
    SQLALCHEMY_TRACK_MODIFICATION = os.environ.get("SQLALCHEMY_TRACK_MODIFICATION") 
    
    @staticmethod
    def init_app(app):
        print("inside init_app")
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")

class IntegrationConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("INT_DATABASE_URI")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "integration": IntegrationConfig,
    "production": ProductionConfig,
    
    "default": DevelopmentConfig
}