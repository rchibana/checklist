__author__ = 'rchibana'

from app import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=True)
    password = db.Column(db.String(), default=datetime.now)

    def __repr__(self):
        return '<User %s>' % self.username
