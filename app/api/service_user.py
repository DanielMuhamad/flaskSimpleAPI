from app.api import api, ns
from flask_restplus import Resource

@ns.route('/users')
class UserAPI(Resource):
    def get(self):
        return {
            "test": "test user"
        }