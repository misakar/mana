---------mana-----------
===
### : my flask toolkit : help me generate my flask app.

## flask in my heart

    flask是一个非常自由的框架，这种自由体现在选择上，可以说没有任何限制，你可以选择你想要的数据库
    你想用的扩展。如果没有，你可以自己写一个.

## But Choose is Difficult

    I think;

## toolkit

    每个flask开发者都有自己熟练的一套工具

## generate

    不用每次重复的创建文件目录，集成、初始化扩展。

## So: mana

    mana = my:toolkit + generate

## install mana

    $ pip install mana0

mana 目前只支持mac和Linux系统。<br/>

## 使用mana 😄
### init your project

    $ mana init project_name

你已经创建了你的目录结构(如图)<br/>

                    |-app/              ---- __init__.py
                    |-test/                  models.py
    project_name -  |-config.py              views.py
                    |-requirement.txt        forms.py
                    |-README.md              templates
                    |                        static

并且在相关文件中预填了代码<br/>

### install your flask extensions
在 requirement.txt 中写入你希望安装的扩展的名称

    $ mana install --venv

这将创建一个名称为venv的虚拟环境并在该虚拟环境中安装扩展<br/>
如果你希望在全局环境中安装扩展，你可以关闭 --venv 选项

    $ mana install --no-venv

那么你的扩展就会被安装到全局中<br/>


### work with sql
对于sql数据库的处理, flask-sqlalchemy 是我最常用的扩展，使用mana可以帮助我快速集成、初始化扩展

    $ mana sql project_name

接下来，你只需要专心于models.py的数据库设计与编码了<br/>


### create manage.py
还可以使用mana创建manage.py集成flask-script和flask-migrate管理我们的项目和进行数据库迁移与更新

    $ mana manage project_name

现在可以使用manage.py进行数据库迁移和更新了

    $ python manage.py db init
    $ python manage.py db migrate -m "v1.0"
    $ python manage.py db upgrade

使用manage.py启动数据库

    $ python manage.py runserver

使用shell环境

    $ python manage.py shell

如果你希望在shell中自动导入模块(ex: 导入User)的话:

    from app.models import User

    def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app,
        db=db,
        User=User
    )

这样就可以了<br/>


## my flask toolkit
处理sql数据库: [flask-sqlalchemy](https://github.com/mitsuhiko/flask-sqlalchemy)<br/>
处理登录: [flask-login](https://github.com/maxcountryman/flask-login)<br/>
进行数据库迁移: [flask-migrate](https://github.com/miguelgrinberg/Flask-Migrate)<br/>
进行项目管理: [flask-script](https://github.com/smurfix/flask-script)<br/>
后台管理: [flask-admin](https://github.com/flask-admin/flask-admin)<br/>

## future
1. 自动处理登录<br/>
2. init 更加细化: 单文件，无蓝图组织，蓝图组织<br/>
3. 自动添加测试单元<br/>


## 进度

	2015-0910: have an idea
	----------------------------------------------------
	2015-0911: mana init & mana install & mana sql
	----------------------------------------------------
	2015-0912: mana manage
	----------------------------------------------------
	2015-0920: clean this repo..
	----------------------------------------------------
	2015-1024: hackathon hack
	----------------------------------------------------
	2015-1024: mana init update, review my old code :(

## powered by click
[click源码](https://github.com/mitsuhiko/click) 😄  <br/>

    click 是flask作者的一个开源项目

[click文档](http://click.pocoo.org/5/)👌 <br/>
