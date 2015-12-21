mana
====

   the missing startapp command for Flask

![mana](http://7xj431.com1.z0.glb.clouddn.com/mana22.gif)

## 更多mana操作请看视频(不是很清楚啦)

YouKu[广告很烦人]: http://v.youku.com/v_show/id_XMTQxNzI0MjA3Mg==.html <br/>

![mana](https://raw.githubusercontent.com/neo1218/mana/master/artwork/images-2.jpeg)

## 安装 mana
#### 1. pip 安装

    $ pip install mana

#### 2. 源码安装

    $ git clone https://github.com/neo1218/mana
    $ cd mana
    $ sudo pip install .

## mana init {project_name}::构建基本项目

    $ mana init my_project

:result:
![mana init](http://7xj431.com1.z0.glb.clouddn.com/mana_init) <br/>

现在基本框架已经搭建好了，你需要安装flask扩展，默认的扩展已经写在
requirement.txt 中了，所以你只要:

    $ pip install -r requirement.txt

扩展安装完毕，你就可以运行你的flask project了!

    $ python manage.py runserver

访问 http://127.0.0.1:5000/test/ mana会告诉你一切正常!<br/>


## mana sqlinit {project_name}::构建含sql数据库的项目

    $ mana sqlinit sql_project

:result:
![mana sqlinit](http://7xj431.com1.z0.glb.clouddn.com/mana_sqlinit)<br/>
同样，你需要安装flask扩展。<br/>
sqlinit 构建的项目使用蓝图来组织flask
project，main为主蓝图, mana提供了blueprint命令可以自动帮你创建和注册flask蓝图。<br/>

现在，你可以创建、迁移、更新你的数据库了(默认是sqlite数据库)

    $ python manage db init
    $ python manage.py db migrate -m ""
    $ python manage.py db upgrade

data-dev.sqlite 就是你的数据库文件<br/>

如果你希望<strong>更改数据库类型</strong>, 你只需要更改配置文件(config.py)中的
SQLALCHEMY_DATABASE_URI 配置项，下面是常用数据库的uri列表:

| database | uri |
| ------------- |-------------|
| postgres |postgresql://scott:tiger@localhost/mydatabase|
| mysql |mysql://scott:tiger@localhost/mydatabase|
| oracle |oracle://scott:tiger@127.0.0.1:1521/sidname|
| sqlite |sqlite:////absolute/path/to/foo.db|

### 关于配置文件
sqlinit
构建的配置文件(config.py)独立出3种配置环境(开发、测试、生产)，分别对应着三个类，并从基类中继承共同的配置

### 关于manage.py
manage.py 使用 flask-script,flask-migrate 对flask项目进行管理

|命令|功能|
|------|-------|
|python manage.py runserver|运行flask项目|
|python manage.py db init|创建数据库迁移目录|
|python manage.py db migrate -m ""|进行数据库迁移|
|python manage.py db upgrade|依据迁移更新数据库|
|python manage.py test|运行测试目录test|

可以在manage.py的 make_shell_context() 中写入相关的类,这样就可以在 python
manage.py shell 中直接使用。比如:

    from app.models import User
    def make_shell_context():
        return dict(
            app = app,
            db = db,
            User = User
        )

运行:

    $ python manage.py shell
    >> User
    app.models.User

## mana blueprint {blueprint_name}

    $ cd sql_project
    $ cd app
    $ mana blueprint auth

:result:
![mana blueprint](http://7xj431.com1.z0.glb.clouddn.com/mana_blueprint) <br/>
mana blueprint 会自动帮你创建蓝图，并把蓝图注册在app/--init--.py中

## powered by click
click: https://github.com/mitsuhiko/click

## flask with mana
mana
的灵感来源于django的startapp命令。的确flask不是很适合开发大型项目，但是flask基于一个超级强大的库werkzeug，这使得用
flask写项目在某些方面的体验是比django好的(比如django需要正则写url，flask用route装饰器就可以了)。所以我希望通过mana，
既可以让我们体验flask的强大，又能方便、快速的构建项目和管理数据库。<br/>
但是，现在的mana还很小，功能还很少。目前只是可以快速的构建项目和数据库。下一步计划像django-admin一样自带管理后台，这样
操作数据库的时候就会方便很多!<br/>
