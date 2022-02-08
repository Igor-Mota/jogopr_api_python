from email import header
from pickle import TRUE
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
        token = request.headers['Authorization']
        autorized = auth_middleware.authorization(token)
        full_data = dict(headers=autorized, body=body)
        return activity.create(full_data)
