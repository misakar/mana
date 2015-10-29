# coding: utf-8

"""
    _deploy.py
    ~~~~~~~~~~

        部署文件
"""

_wsgi_py = '''# coding: utf-8

from manage import app


if __name__ == "__main__":
    app.run(host="%s", port=%d)
'''
