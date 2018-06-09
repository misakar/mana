# coding: utf-8

"""
    _manage_basic.py
    ~~~~~~~~~~~~~~~~

        basic manage.py code

"""

_manage_rest_code = '''# coding: utf-8

"""
    manage.py
    ~~~~~~~~~
    : [intro]
    : -- xueer backend management
    : [shell]
      -- python manage.py db init
      -- python manage.py db migrate
      -- python manage.py db upgrade
      -- python manage.py runserver
      -- python manage.py test
      -- python manage.py freeze
"""

import os
import sys
from app import app,db
from flask_script import Manager,Shell
from app.models import Role,User
from flask_migrate import Migrate,MigrateCommand

manager=Manager(app)
migrate=Migrate(app,db)

COV = None
if os.environ.get('APP_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


def make_shell_context():
    """自动加载环境"""
    return dict(app=app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)



@manager.command
def test(coverage=True):
    """Run the unit tests."""
    import sys
    if coverage and not os.environ.get('APP_COVERAGE'):
        os.environ['APP_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.erase()
    sys.exit(0)


if __name__ == '__main__' :
    if sys.argv[1] == 'test' or sys.argv[1] == 'lint':
        os.environ['APP_CONFIG'] = 'testing'
    manager.run()

'''
