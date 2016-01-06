__author__ = 'rchibana'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'checklist.db')
PRIORITYS = [(1, 'Normal'), (2, 'High')]
