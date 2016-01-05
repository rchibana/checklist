__author__ = 'rchibana'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'checklist.db')


PRIORITYS =['HIGH', 'NORMAL']