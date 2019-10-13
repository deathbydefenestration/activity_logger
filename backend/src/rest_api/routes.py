from datetime import datetime
from decimal import Decimal

from flask import Blueprint, jsonify, request, g

from src.db_models.activity import Activity

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/activities', methods=['POST'])
def activities():
    api_input = request.get_json()
    response = None
    if api_input.get('operation') == 'add':
        response = _add_activity(api_input)
    return response


def _add_activity(api_input):
    try:
        activity = Activity(
            athlete_id=api_input.get('athlete_id'),
            type=api_input.get('activity_type'),
            date=datetime.strptime(api_input.get('activity_date'), '%Y-%m-%d'),
            distance=Decimal(api_input.get('activity_distance')),
            duration=Decimal(api_input.get('activity_duration'))
        )
        g.db.session.add(activity)
        g.db.session.commit()

        return _api_success()
    except Exception as e:
        return _api_error(error_message=str(e))


def _api_success(code=200):
    response = jsonify({})
    response.status_code = code
    return response


def _api_error(error_message, error_code=400):
    response = jsonify({'error': error_message})
    response.status_code = error_code
    return response
