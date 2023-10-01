from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

DATABASE_URI = os.getenv("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", default="014145ea5815464ebca08240f2b8bbc6")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = "id"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
