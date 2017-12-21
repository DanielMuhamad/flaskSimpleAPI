from flask import Flask, Blueprint
from app.api import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1724@localhost/sapi_db'

# #url
# @api.route('/index')
# class HelloWorld(Resource):
#     def get(self):
#         return {'object': 'hello world!'}

#     def post(self):
#         return {'obj': 'hello post'}

from app import models
from app.api.service_product import ns as product_api
from app.api.service_user import ns as user_api

blueprint = Blueprint('api', __name__, url_prefix='/service')
api.init_app(blueprint)

api.add_namespace(user_api)
api.add_namespace(product_api)

app.register_blueprint(blueprint)