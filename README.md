mana
====

    the missing startapp command for Flask

![mana](http://7xj431.com1.z0.glb.clouddn.com/mana3.gif)

## more mana options please see the movie

YouKu: http://v.youku.com/v_show/id_XMTQxNzI0MjA3Mg==.html <br/>
YouTuBe:

![mana](https://raw.githubusercontent.com/neo1218/mana/master/artwork/images-2.jpeg)

## install mana

    $ pip install mana

## mana init <project_name>
:example:

    $ mana init my_project

:result: <br/>
![mana init](http://7xj431.com1.z0.glb.clouddn.com/mana_init) <br/>

after init, you need to install flask extensions

    $ pip install -r requirement.txt

now, you can run your flask project(default in Debug mode):

    $ python manage.py runserver

and go to http://127.0.0.1:5000/test to see everything is ok :) <br/>
now, you just need to open <app/views.py> and write your views !


## mana sqlinit <project_name>
:example:

    $ mana sqlinit my_project

:example: <br/>
![mana sqlinit](http://7xj431.com1.z0.glb.clouddn.com/mana_sqlinit)<br/>
mana sqlinit use create_app funciton to create flask app (see: app/--init--.py), and use blueprint to
organize flask project. mana also provide blueprint command to help you
automatically create and register flask blueprint. <br/>

now, you can create your database(default database is sqlite3)

    $ python manage db init
    $ python manage.py db migrate -m ""
    $ python manage.py db upgrade

and data-dev.sqlite is your database file name <br/>

if you want <strong>change database</strong>, just modify the
SQLALCHEMY_DATABASE_URI in config file(config.py), here is a list of
sql database uri: <br/>

| database | uri |
| ------------- |-------------|
| postgres |postgresql://scott:tiger@localhost/mydatabase|
| mysql |mysql://scott:tiger@localhost/mydatabase|
| oracle |oracle://scott:tiger@127.0.0.1:1521/sidname|
| sqlite |sqlite:////absolute/path/to/foo.db|

## mana blueprint <blueprint_name>
:example:

    $ cd sql_project
    $ cd app
    $ mana blueprint auth

:result: <br/>
![mana blueprint](http://7xj431.com1.z0.glb.clouddn.com/mana_blueprint) <br/>
and auth blueprint is automatically registed in app/--init--.py

## powered by click
click: https://github.com/mitsuhiko/click

## well, mana still in developement, and looking forward to your help
