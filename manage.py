# coding=utf-8
#! ./kt/bin/python

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app(config_name='default')
migrate = Migrate(app, db)

def _make_context():
    return dict(app=app, db=db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
