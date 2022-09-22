from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os


db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import main
    app.register_blueprint(main)

    return app