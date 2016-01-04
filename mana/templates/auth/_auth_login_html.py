# coding: utf-8

_auth_login_html_code = '''# coding: utf-8

<html>
    <body>
        <h1>simple auth login</h1>
        <div class="form">
            <form method="post">
            {{ form.hidden_tag() }}
            {{ form.username }}
            {{ form.password }}
            {{ form.submit }}
            </form>
        </div>
    </body>
</html>
'''
