#coding: utf-8
_rest_test_code='''# coding: utf-8
"""
    test_api.py
    ```````````
    : api 功能测试
"""

import unittest
import json
from base64 import b64encode
from flask import url_for
from app import create_app,db
from app.models import Role,User


class APITestCase(unittest.TestCase):
    def setUp(self):
        """
        初始化测试
        """
        self.app = create_app("testing")
        self.app.config.update(
            SERVER_NAME='localhost:5000',
            debug=False
        )
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client()

    def tearDown(self):
        """
        测试结束, 清空环境
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_api_headers(self, username, password):
        """
        username:password headers
        """
        return {
            'Authorization': 'Basic ' + b64encode(
                (username + ':' + password).encode('utf-8')
            ).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_token_headers(self, token):
        """
        token headers
        """
        return {
            'Authorization': 'Basic ' + b64encode((token + ':').encode('utf-8')).decode("utf-8"),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    def get_normal_header(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }


    def test_admin_token(self):
        """
        test admin user token
        """
        u = User(
            email='admin@admin.com',
            password=b64encode(b'muxi304'),
            role_id=2
        )
        db.session.add(u)
        db.session.commit()

        res = self.client.get(
            url_for('api.get_token'),
            headers=self.get_api_headers(
                'admin@admin.com', 'muxi304'
            )
        )
        user_token = eval(res.data).get('token')
        u = User.query.filter_by(email='admin@admin.com').first()
        expect_token = u.generate_auth_token()
        self.assertTrue(str(user_token) == str(expect_token))

    def test_normal_token(self):
        """
        test normal user token
        """
        u = User(
            email='3480437308@qq.com',
            password=b64encode(b'muxi304'),
            role_id=3
        )
        db.session.add(u)
        db.session.commit()
        token = u.generate_auth_token()

        res = self.client.get(
            url_for('api.get_token'),
            headers=self.get_api_headers(
                '3480437308@qq.com', 'muxi304'
            )
        )
        user_token = eval(res.data).get('token')
        u = User.query.filter_by(email='3480437308@qq.com').first()
        expect_token = u.generate_auth_token()
        self.assertTrue(str(user_token) == str(expect_token))


    def test_404(self):
        """
        test 404 response
        """
        res = self.client.get(
            '/wrong/url',
            headers=self.get_api_headers('email', 'password')
        )
        self.assertTrue(res.status_code == 404)

    def test_401(self):
        """
        test 401 response
        """
        res = self.client.put(url_for('api.user',id=1))
        self.assertTrue(res.status_code == 401)


    def test_create_and_get_user(self):
        res=self.client.post(url_for("api.user",id=0),
                             headers=self.get_normal_header(),
                             data=json.dumps({
                                   'email': '3480437308@qq.com',
                                   'password':str(b64encode(b'muxi304')),
                                   'role_id': 2
                               }))
        self.assertTrue(res.status_code==200)

        res=self.client.get(url_for("api.user",id=1),
                            headers=self.get_normal_header())
        self.assertTrue(res.status_code==200)

    def test_update_and_delete_user(self):
        admin = User(
            email='admin@admin.com',
            password=b64encode(b'muxi304'),
            role_id=3
        )

        moderator=User(
            email='moderator@moderator.com',
            password=b64encode(b'muxi304'),
            role_id=2
        )

        normal_user=User(
            email='normaluser@normaluser.com',
            password=b64encode(b'muxi304'),
            role_id=1
        )
        db.session.add(admin)
        db.session.commit()
        db.session.add(moderator)
        db.session.commit()
        db.session.add(normal_user)
        db.session.commit()

        res=self.client.put(url_for("api.user",id=3),
                            headers=self.get_token_headers(
                                admin.generate_auth_token()
                            ),
                            data=json.dumps({
                                "email":"admin_updated_email@gmail.com",
                                "password":str(b64encode(b"you never know"))
                            }))
        updated_user=User.query.get_or_404(3)
        self.assertTrue(updated_user.email=="admin_updated_email@gmail.com")

        res = self.client.put(url_for("api.user",id=3),
                              headers=self.get_token_headers(
                                  moderator.generate_auth_token()
                              ),
                              data=json.dumps({
                                  "email": "moderator_updated_email@gmail.com"
                              }))
        updated_user = User.query.get_or_404(3)
        self.assertTrue(updated_user.email == "moderator_updated_email@gmail.com")

        res = self.client.delete(url_for("api.user", id=3),
                              headers=self.get_token_headers(
                                  moderator.generate_auth_token()
                              ))
        self.assertTrue(res.status_code == 403)

        res = self.client.delete(url_for("api.user", id=3),
                              headers=self.get_token_headers(
                                  admin.generate_auth_token()
                              ))
        self.assertTrue(res.status_code == 200)




'''