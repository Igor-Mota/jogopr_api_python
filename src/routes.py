from .controllers import authenticate
from flask import request, jsonify
from flask_cors import CORS, cross_origin


def routes(app):
    @app.route('/auth/register', methods=['POST'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json'])
    def register():
        body = request.get_json()
        return jsonify(authenticate.register(body))

    @app.route('/list', methods=['GET'])
    @cross_origin(origin='*', headers=['Content-Type', 'application/json'])
    def list_teachers():
        return jsonify(authenticate.get_all_teachers())
