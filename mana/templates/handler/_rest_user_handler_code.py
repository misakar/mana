# coding: utf-8

_rest_user_handler_code = '''# coding: utf-8

from . import api
from app.models import User,db
from flask_restful import Resource,reqparse,Api
from app.decorators import admin_required,moderator_required


api=Api(api,prefix="/user")


parser = reqparse.RequestParser()
# parser是post请求中的参数要求
parser.add_argument('password',type=str,required=True,help="base64 encoded password required")
parser.add_argument('role_id',type=int,help="user role id")
parser.add_argument('email', type=str, required=True,help="user email required")


#parser_copy是put请求中的参数要求
parser_copy = parser.copy()
parser_copy.replace_argument('email', type=str,help="the new email")
parser_copy.replace_argument('password',type=str,help="the new encoded password")


class UserHandlerClass(Resource):

    def get(self,id):
        u=User.query.get_or_404(id)
        return u.to_json(),200

    def post(self,id):
        args=parser.parse_args(strict=True)
        u=User(email=args["email"],password=args["password"],
             role_id=(args["role_id"] if args["role_id"] else 2))
        db.session.add(u)
        db.session.commit()
        return {"msg":"user created"},200

    @admin_required
    def delete(self,id):
        u=User.query.get_or_404(id)
        db.session.delete(u)
        db.session.commit()
        return {"msg":"user delete successful"},200

    @moderator_required
    def put(self,id):
        u = User.query.get_or_404(id)
        args = parser_copy.parse_args(strict=True)
        u.email=args["email"] if args["email"] else u.email
        if args["password"] is not None and args["password"]  != "":
            u.password=args["password"]
        db.session.add(u)
        db.session.commit()
        return {"msg":"user updated"},200

api.add_resource(UserHandlerClass, '/<int:id>/',endpoint="user")


'''