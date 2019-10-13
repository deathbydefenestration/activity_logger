from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/hello', methods=['POST', 'GET'])
def hello():
    response = jsonify({'hello': 'me'})
    response.status_code = 200
    return response
