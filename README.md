mana
==
the missing startproject command for Flask <br/>

## what is mana
mana just like django startproject command, help you fast build and manage your flask project!

## mana command set
### => mana startproject (project_name)
<strong>mana startproject</strong> command is powerful, it can help you build a sql database driven project, and provide a CRUD admin site.
#### mana startproject (project_name)

    $ mana startproject myblog

it create a flask project called myblog, and it structure is:

    myblog/ => requirement.txt
               manage.py
               config.py

               app/ => __init__.py
                       models.py
                       templates/ => main/
                                     auth/
                                     admin/
                       static/ => img/
                                  css/
                                  js/
                       admin/
                       auth/
                       main/ => __init__.py
                                forms.py
                                views.py

#### install flask extensions

    $ virtualenv myblog_venv
    $ source myblog_venv/bin/activate
    $ pip install -r requirement.txt

#### setup sql database
(default sql database is sqlite3, you can change it by edit config.py)

    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade

create user roles

    $ python manage.py shell
    >> Role.insert_roles()
    >> quit()

#### create admin user

    $ python manage.py admin
    \_admin username:
    \_admin email:
    \_admin password:

#### run the project
now, you can run myblog:

    $ python manage.py runserver

and goto http://127.0.0.1:5000/admin <br/>
![admin login](http://7xj431.com1.z0.glb.clouddn.com/manalogin2)<br/>

after login as an administrator, you can see the CRUD admin site: <br/>
![admin site](http://7xj431.com1.z0.glb.clouddn.com/manaadmin22) <br/>
![admin site2](http://7xj431.com1.z0.glb.clouddn.com/manaadmin222)<br/>

### => mana blueprint (blueprint_name)
<strong>mana blueprint</strong> command can automatic create and
register a flask blueprint, go to the app folder:

    $ mana blueprint book

and the book blueprint is created and registed in <code>app/__init__.py</code>.

### => mana init (project_name)
<strong>mana init</strong> command can fast build a tiny flask app, which structure is:
![mana init](http://7xj431.com1.z0.glb.clouddn.com/manainit) <br/>
after init, you should install flask extensions(highly recommend use [virtualenv](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)), just type <code>$ pip install -r requirement.txt</code> <br/>
you can run your project by <code>$ python manage.py runserver</code> <br/>
now, you can goto http://127.0.0.1:5000/test and check everything is ok :)

### => mana version
show the version info: latest version: 3.9

## install mana
#### 1. install by pip

    $ pip install mana

#### 2. install from source

    $ git clone https://github.com/neo1218/mana
    $ cd mana
    $ sudo pip install .

## flask extensions used by mana
### management

+ Flask-Script

### sql database

+ Flask-Migrate
+ Flask-Sqlalchemy

### auth

+ Flask-Login
+ Flask-Bcrypt

### form

+ Flask-WTF

### admin

+ Flask-Admin

## LICENSE
MIT: see [LICENSE](https://github.com/neo1218/mana/blob/master/LICENSE) for more detail
