from .controllers import authenticate
from flask import request, jsonify


def routes(app):
    @app.route('/auth/register', methods=['POST'])
    def register():
        body = request.get_json()
        return jsonify(authenticate.register(body))

    @app.route('/list', methods=['GET'])
    def list_teachers():
        return jsonify(authenticate.get_all_teachers())
