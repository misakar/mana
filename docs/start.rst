.. _genindex:

flask with mana
=============================
::

    在这篇文档中,你将知道如何使用mana构建和管理flask项目,
    假设你已经安装了mana，具体见安装文档


使用mana构建你的项目吧！
----------------------------------
在命令行中输入::

    $ mana init <project_name>

这时你需要键入配置选项::

    \__ SQL Database[Y/N]:
    \__ Admin Site[Y/N]:

SQL Database: 是否需要sql数据库(默认是sqlite数据库，如果需要更改请参见 **数据库** )。

Admin Site: 是否需要管理后台，如果你选择了配置管理后台，那么会让你继续配置管理员用户和密码::

    \__ admin username:
    \__ admin password:

配置结束后，你的flask项目就构建好啦! 你可以运行::

    $ python manage.py runserver

访问 http://127.0.0.1:5000/test/，你就可以看到可爱的test路由啦!

mana 构建1: 基本结构
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $ mana init <project_name>

    start init your project
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





