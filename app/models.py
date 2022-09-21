from app import db
from datetime import datetime


class ShortUrls(db.Model):
    """Class for Table ShortURL"""
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_id = db.Column(db.String(50), nullable=False, unique=True)
    create_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    clicks = db.Column(db.Integer, nullable=False, default=0)

    def __str__(self):
        return self.short_id