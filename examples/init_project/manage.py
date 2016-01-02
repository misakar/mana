# coding: utf-8

"""
    manage.py
    ~~~~~~~~

    shell:
        python manage.py shell
    run server:
        python manage.py runserver
            -d 开启调试模式
"""

import sys
from app import app
from flask.ext.script import Manager, Shell

"""编码设置"""
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)


def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app
    )


manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()

