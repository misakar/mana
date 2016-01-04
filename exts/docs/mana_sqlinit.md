mana sqlinit {project_name}
===

## Command

    $ mana sqlinit project_name
    $ pip install -r requirement.txt

## Result
![mana sqlinit](http://7xj431.com1.z0.glb.clouddn.com/mana_sqlinit_result) <br/>
and you can run

    $ python manage.py runserver

to run your project.

## Usage

    sqlinit command help you fast create sql database project(default database
    is sqlite3) and use flask blueprint to organize your project.

### create database
you can use manage.py to create and manage your database<br/>

1. create migration

    $ python manage.py db init

2. first migrate

    $ python manage.py db migrate -m "init"

    after migrate, you can see the data-dev.sqlite file is your database file

3. upgrade database

    $ python manage.py db upgrade

### change database
if you want use MySQL or other databases, simplely change the config
"SQLALCHEMY_DATABASE_URI" in config.py, and here is the uri list:

| Database | URI|
|-------|-------|
|Postgres|postgresql://scott:tiger@localhost/mydatabase|
|MySQL|mysql://scott:tiger@localhost/mydatabase|
|Oracle|oracle://scott:tiger@127.0.0.1:1521/sidname|
|SQLite|sqlite:////absolute/path/to/foo.db|

### add blueprint
if you want register another blueprint, you can use mana blueprint command.<br/>
go to the app floder:

    $ mana blueprint auth

and auth blueprint will be created and registed in app !<br/>
detail: https://github.com/neo1218/mana/blob/master/docs/mana_blueprint.md

## More detail
### config.py
the configuration file is divided into three environments

    Devlop, Test, Product

and corresponding to the three classes.<br/>
their common configuration are defined in Config class.

### manage.py
you can use manage.py run and manage your project
#### python manage.py runserver

    run your project

#### python manage.py shell

    get into shell context

ps: if you want auto import your model in shell context, just add your model
into manage.py/make_shell_context .
