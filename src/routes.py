from .controllers import authenticate
from flask import request, jsonify
from flask_cors import CORS, cross_origin


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

    @app.route('/list', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json'])
    def list_teachers():
        return jsonify(authenticate.get_all_teachers())
