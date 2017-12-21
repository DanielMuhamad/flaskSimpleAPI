from flask_restplus import Api, Resource
api = Api(version='1.0', title='simple API',
    description='A Simple API'
)
ns = api.namespace("v0.1", "SimpleAPI")