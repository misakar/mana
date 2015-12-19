mana
====

    the missing startapp command for Flask

![mana](http://7xj431.com1.z0.glb.clouddn.com/mana3.gif)

## 更多mana操作请看视频(不是很清楚啦)

YouKu: http://v.youku.com/v_show/id_XMTQxNzI0MjA3Mg==.html <br/>

![mana](https://raw.githubusercontent.com/neo1218/mana/master/artwork/images-2.jpeg)

## 安装 mana

    $ pip install mana

## mana init {project_name}::构建基本项目

    $ mana init my_project

:result:
![mana init](http://7xj431.com1.z0.glb.clouddn.com/mana_init) <br/>

现在基本框架已经搭建好了，你需要安装flask扩展，默认的扩展已经写在
requirement.txt 中了，所以你只要:

    $ pip install -r requirement.txt

扩展安装完毕，你就可以运行你的flask project了!

    $ python manage.py runserver

访问 http://127.0.0.1:5000/test，mana会告诉你一切正常!<br/>


## mana sqlinit {project_name}::构建含sql数据库的项目

    $ mana sqlinit sql_project

:result:
![mana sqlinit](http://7xj431.com1.z0.glb.clouddn.com/mana_sqlinit)<br/>
同样，你需要安装flask扩展。<br/>
sqlinit 构建的项目采用了flask工厂函数来创建flask app，使用蓝图来组织flask
project，mana提供了blueprint命令可以自动帮你创建和注册flask蓝图。<br/>

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
