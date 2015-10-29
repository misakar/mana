# coding: utf-8

"""
    mana
    ~~~~

        fast generate flask project

        copyright: (c) 2015 by neo1218.
        :license: MIT, see LICENSE for more details.

        :version 1.0
        mana init project_name                 # init your project
        mana install                           # install your flask extensions
            --venv                             # with virtualenv
        mana sql project_name                  # integrate with flask-sqlalchemy
        mana manage project_name               # create manage.py to manage the project

        :version 2.0
        mana blue book                         # create a blueprint book, automatic regiest blueprint
            --prefix                           # url_prefix of blueprint

        :version 2.1
        mana deploy wsgi                       # deploy your flask application on wsgi server

"""

import click
import os
# import code templates
from templates._base import _init_py, _init_sql_py
from templates._config import _config_sql_py, _config_py
from templates._sql import _sql_py
from templates._management import _management_py
from templates._blueprint import _blueprint_py
from templates._deploy import _wsgi_py


###################################################
project = "my_project"  # store project info      #
# project name can help us find the basic pwd     #
###################################################


def make_tuple(name, count):
    """
	格式化元组工厂函数
	:param name:
	:param count:
	"""
    format_tuple = []
    for i in range(count):
        format_tuple.append(name)
    return tuple(format_tuple)


def fill_file(floder, filename, pre_code):
    """
	文件中填入预填代码:
	预填代码从templates模版中获取
	:param project_name
	:param filename
	:param pre_code
	"""
	# :path 当前路径
	# open the file path::project_name::filename and is "w+"
	# write the pre_code into file
    path = os.popen('pwd').readlines()[0][0:-1]
    fo = open("%s/%s/%s" % (path, floder, filename), "w+")
    fo.write(pre_code)
    fo.close


"""use click:)"""
""":version 1.0"""

@click.group()
def cli():
    """fast generate flask app 🍺" """
    pass


@click.command()
@click.argument('project_name')
def init(project_name):
    """
	init your project
    """
    # :param project_name 你项目的名字
    # :default 默认是 "my_project"
    # 将 project 声明为全局变量，用于存储项目基本信息
    global project
    project = project_name

	# 在python中执行shell命令
    os.system("mkdir %s" % project_name)
    os.system("touch %s/README.md %s/config.py %s/requirement.txt" \
            % make_tuple(project_name, 3))
    os.system("mkdir %s/app/ %s/test/" \
            % make_tuple(project_name, 2))
    os.system("touch %s/app/__init__.py %s/app/models.py %s/app/views.py %s/app/forms.py" % \
            make_tuple(project_name, 4))
    os.system("mkdir %s/app/templates/ %s/app/static/" % \
            make_tuple(project_name, 2))
    os.system("cd ..")

    # happy coding
	# 调用 fill_file 函数
	# 初始化的时候调用模版预填代码
    fill_file(project_name, 'config.py', _config_py)
    fill_file(project_name, 'app/__init__.py', _init_py)

    click.echo("init ... done!")


@click.command()
@click.option('--venv', default=True, help="install your flask extensions into virtualenv")
def install(venv):
    """
	install your flask extensions
    """
    # 安装flask扩展
	# :venv 虚拟环境 默认是 False
	# :--venv 创建虚拟环境，并在虚拟环境下安装扩展
	# :--no-venv 在全局环境中安装扩展
	# 需要在 'requirement' 文件中预填扩展
	# :example
	# 	Flask==0.10
    if venv:
        click.echo("creating venv")
        os.system("virtualenv venv")
        os.system(". venv/bin/activate")

        click.echo("install extensions")
        os.system("pip install -r requirement.txt")
        click.echo("install ... done!")
    else:
        click.echo("install extensions")
		# use sudo
        os.system("sudo pip install -r requirement.txt")
        click.echo("install ... done!")


@click.command()
@click.argument('project_name')
def sql(project_name):
    """
	integrate flask-sqlalchemy
    """
    # 自动集成flask-sqlalchemy扩展
    # :param project_name 项目的名称
    fill_file(project_name, 'config.py', _config_sql_py)
    fill_file(project_name, 'app/__init__.py', _init_sql_py)
    fill_file(project_name, 'app/models.py', _sql_py)
    click.echo("integrate flask-sqlalchemy ... done!")


@click.command()
@click.argument('project_name')
def manage(project_name):
    """
	create manage.py help me:)
    """
    # 创建 manage.py 文件
    # 调用 fill_file 函数
    fill_file(project_name, 'manage.py', _management_py)
    click.echo("create ... done!")


""":version 2.0"""
@click.command()
@click.argument('project_name')
@click.argument('blueprint_name')
@click.option('--prefix', default=False, help="the url_prefix of blueprint")
def blue(project_name, blueprint_name, prefix):
    """
    create blueprint
    """
    # 创建蓝图
    # :ex mana blue book
    #     book = Blueprint('book', __name__, template_folder='templates', static_folder='static')
    #     app.register_blueprint(book)
    # :ex mana blue book --prefix="/book"
    #     app.register_blueprint(book, url_prefix="/book")
    # :ex mana blue book --subdomain="book"
    #     app.register_blueprint(book, subdomain='book')
    click.echo("create flask Blueprint obj %s" % blueprint_name)
    # create blueprint folder
    os.system("cd %s/app && mkdir %s" % (project_name, blueprint_name))
    # create blueprint files
    os.system("cd %s/app/%s && touch __init__.py views.py forms.py" % (project_name, blueprint_name))
    # create Blueprint obj:: blueprint
    fill_file(project_name+'/app/'+blueprint_name, '__init__.py', _blueprint_py % make_tuple(blueprint_name, 2))
    # register blueprint
    # blue命令可以注册多个蓝图
    # 为了更灵活的处理蓝图的注册,蓝图注册不预填代码模版
    # 而是直接插入代码片段,进行注册
    #   :ex: "app.register_blueprint('%s')" % blueprint_name + _init_py
    if prefix:
        blue_code = "app.register_blueprint('%s', url_prefix='%s')" % (blueprint_name, prefix)
    else:
        blue_code = "app.register_blueprint('%s')" % blueprint_name
    # app:__init__.py 在使用蓝图后，更多的是用于分发请求
    fill_file(project_name, 'app/__init__.py', _init_py + blue_code)
    # ...done !
    click.echo("create ... done!")


""":version 2.1"""
@click.command()
@click.argument('project_name')
@click.option('--host')
@click.option('--port', type=int)
def deploy(project_name, host, port):
    """deploy your flask application"""
    click.echo("create wsgi file")
    os.system("cd %s && touch wsgi.py" % project_name)
    fill_file(project_name, 'wsgi.py', _wsgi_py % (host, port))


###########################
# mana command set
cli.add_command(init)
cli.add_command(install)
cli.add_command(sql)
cli.add_command(manage)
cli.add_command(blue)
cli.add_command(deploy)
###########################
