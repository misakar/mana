# coding: utf-8

"""
    _manage_admin.py

"""

_manage_admin_code = '''# coding: utf-8

import sys
import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app import db, app
from app.models import User, Role

# 编码设置
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """自动加载环境"""
    return dict(
        app = app,
        db = db,
        User = User,
        Role = Role
    )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """运行测试"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def admin():
    """add admin user"""
    from getpass import getpass
    username = raw_input("\_admin username: ")
    email = raw_input("\_admin email: ")
    password = getpass("\_admin password: ")
    u = User(
        email = email,
        username = username,
        password = password,
        role_id = 2
    )
    db.session.add(u)
    db.session.commit()
    print "<admin user %s add in database>" % username


if __name__ == '__main__':
    manager.run()

'''
