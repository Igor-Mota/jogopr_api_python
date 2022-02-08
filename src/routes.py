from pickle import TRUE
from tokenize import Number
from .controllers import authenticate, activity
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from .middlewares import auth_middleware


def routes(app):

    CORS(app)

    @app.route('/auth/register', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def register():
        body = request.get_json()
        return jsonify(authenticate.register(body))

    @app.route('/auth/login', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def login():
        body = request.get_json()
        return jsonify(authenticate.login(body))

    @app.route('/activity/create', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json', "Access-Control-Allow-Origin", "*"])
    def create_activity():
        body = request.get_json()
        print(body)
        try:
            token = request.headers['Authorization']
            autorized = auth_middleware.authorization(token)

            if(isinstance(autorized, list) == TRUE):
                print('aqui')
                return 'activity.create(body)'
            else:
                return 'deuu ruim'
        except:
            return 'token is error'
