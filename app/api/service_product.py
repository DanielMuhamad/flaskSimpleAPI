from app.api import api, ns
from flask_restplus import Resource

@ns.route('/products')
class ProductAPI(Resource):
    def get(self):
        return {
            "test": "test wah"
        }