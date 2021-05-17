from flask_restful import Resource
from auth.manager import user_identity
from decorators import admin_required


class UserIdentity(Resource):
    @classmethod
    @admin_required
    def get(cls):
        return user_identity()
