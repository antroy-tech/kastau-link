from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import main
    from app.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app