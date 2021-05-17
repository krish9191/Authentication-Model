from flask_restful import Resource
from flask import request
from auth.manager import update_role
from decorators import admin_required


class RoleUpdate(Resource):
    @admin_required
    def patch(self):
        data = request.get_json()
        return update_role(data['username'], data['role'])