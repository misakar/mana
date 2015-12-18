.. _genindex:

flask with mana
=============================
::

    在这篇文档中,你将知道如何使用mana构建和管理flask项目,
    假设你已经安装了mana，具体见安装文档

.. toctree::
   :maxdepth: 10

使用mana构建你的项目吧！
----------------------------------
在命令行中输入::

    $ mana init <project_name>

这时你需要键入配置选项::

    start init your flask project
    \__ SQL Database[Y/N]:
    \__ Admin Site[Y/N]:

**SQL Database:** 是否需要sql数据库(默认是sqlite数据库，如果需要更改请参见 `含数据库项目构建 <http://0.0.0.0:9527/_build/html/start.html#mana-2>`_ )。

**Admin Site:** 是否需要管理后台，如果你选择了配置管理后台，那么会让你继续配置管理员用户和密码::

    \__ admin username:
    \__ admin password:

配置结束后，你的flask项目就构建好啦! 你可以运行::

    $ python manage.py runserver

访问 http://127.0.0.1:5000/test/，你就可以看到可爱的test路由啦!

mana 构建1: 基本结构
----------------------------------
::

    $ mana init <project_name>

    start init your flask project
    \__ SQL Database[Y/N]: N

这样将构建基础的flask项目, 目录结构如下::

    <project_name> -- manage.py
                  |-- requirement.txt
                  |-- app/ -- | -- templates/ -- test.html
                              | -- static/
                              | -- views.py
                              | -- forms.py
                              | -- __init__.py
并且在相关文件中预填了代码

**requirement.txt** 是你的flask扩展集合，方便你使用pip一次性安装所需的扩展::

    $ pip install -r requirement.txt

强烈推荐在虚拟环境中安装flask扩展!

**manage.py** 是你的flask app启动文件，运行::

    $ python manage.py

即可启动你的flask项目

**app/__init__.py** 文件中创建了flask app，由于是简单的基本构建，你可以将配置写在该文件中。

**app/views.py** 编写你的视图函数吧!

**app/forms.py** 把表单放在这里哦!

**app/templates/** jinja模版文件夹

**app/static/** 静态资源文件夹(img, css, js)

这样，一个命令就可以构建一个基本的flask项目，你可以直接开始编写自己的视图。

基本构建很适合快速开发简单的无数据库的flask应用。


mana 构建2: 含数据库项目构建
----------------------------------
::

    对于一般的大型web项目，数据库是必不可少的，特别是sql数据库。
    mana使用flask-sqlalchemy数据库扩展，使用mana可以快速构建含数据库的flask项目

在命令行中输入::

    $ mana init <project_name>

    start init your flask project
    \__ SQL Database[Y/N]: Y
    \__ Admin Site[Y/N]: N

这样你就创建了含数据库的flask项目，项目结构如下::

    <project_name> -- manage.py
                  |-- requirement.txt
                  |-- config.py
                  |-- app/ -- | -- templates/ -- test.html
                              | -- static/
                              | -- views.py
                              | -- forms.py
                              | -- models.py
                              | -- __init__.py

接下来你可以创建、迁移和更新数据库::

    $ python manage.py db init
    $ python manage.py db migrate -m "init"  # init 为注释内容
    $ python manage.py db upgrade

这时你会发现一个名为 **data-dev.sqlite** 的 **sqlite数据库** 已经创建，并且建立了迁移文件夹 **migration** 。

现在你只需要在 **app/models.py** 中编写你的数据库model了。

**config.py配置文件:**
由于你构建的是含数据库的大型项目，这时就要将配置分离。同时配置文件中又以类的形式，细分了三种环境下的配置::

    Config: 通用配置类
    DevelopmentConfig: 开发环境下配置(default)
    TestingConfig: 测试环境下配置
    ProductionConfig: 生产环境下配置


**更改数据库:** 如果你希望将sqlite更换为mysql数据库，你只需要把 **config.py**
配置文件中相应环境下的数据库uri更改掉即可，常用数据库连接uri

=========   =============================================
Postgres:   postgresql://scott:tiger@localhost/mydatabase
---------   ---------------------------------------------
MySQL:      mysql://scott:tiger@localhost/mydatabase
---------   ---------------------------------------------
Oracle:     oracle://scott:tiger@127.0.0.1:1521/sidname
---------   ---------------------------------------------
SQLite:     sqlite:////absolute/path/to/foo.db
=========   =============================================

mana 构建3: 含管理后台的项目构建
----------------------------------
::

    使用mana可以自动构建含管理后台的项目,

    $ mana init <project_name>
    \__ SQL Database(Y/N): Y
    \__ Admin Site(Y/N): Y

接着会继续配置管理员用户和密码::

    \__ admin username:
    \__ admin password:

然后运行项目::

    $ python manage.py runserver

访问 http://127.0.0.1:5000/admin/ 即可访问管理后台
