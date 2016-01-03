# coding: utf-8

_admin_serializers_code = '''# coding: utf-8

from marshmallow import fields, Serializer


class UserSerializer(Serializer):
    class Meta:
        fields = ("id", "email", "username", "role")

'''
