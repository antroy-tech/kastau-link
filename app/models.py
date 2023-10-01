from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """Class for Table User Information"""

    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    picture = db.Column(db.String(200), nullable=True)
    urls = db.relationship("Url", backref="owner", lazy=True)

    def __repr__(self):
        return self.name


class Url(db.Model):
    """Class for Table Urls"""

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_id = db.Column(db.String(50), nullable=False, unique=True)
    create_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    clicks = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    def __repr__(self):
        return f"Url: {self.id} - {self.short_id}"
