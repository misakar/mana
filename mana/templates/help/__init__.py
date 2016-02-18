# coding: utf-8

help_msg = '''
[click]
the missing startproject command for Flask

[commands]
mana version                    -> show the version info
mana init project_name          -> build a minimal flask project
mana blueprint blueprint_name   -> automatically create and register
                                   a flask blueprint(run under app folder)
mana admin sql_module_name      -> add sqlalchemy modules into admin site
mana startproject project_name  -> build a SQL database driven project,
                                   and provides a CRUD admin dashboard.

[processes]
virtualenv venv && source venv/bin/activate  -> create a virtual environment (optional)
pip install -r requirement.txt               -> install flask extensions

python manage.py db init
python manage.py db migrate
python manage.py db upgrade                  -> setup sql database(default database is sqlite)

python manage.py shell                       -> create roles
>> Role.insert_roles()
>> quit()

python manage.py admin                       -> create admin user
python manage.py runserver (-d)              -> run project(in debug mode)'''

