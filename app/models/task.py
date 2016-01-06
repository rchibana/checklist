__author__ = 'rchibana'

from app import db
from datetime import datetime


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    priority = db.Column(db.String(6))
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task %s>' % self.name
