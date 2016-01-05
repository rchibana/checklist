__author__ = 'rchibana'

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand, Migrate

from app import app, db

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000, use_debugger=True))

if __name__ == '__main__':
    manager.run()