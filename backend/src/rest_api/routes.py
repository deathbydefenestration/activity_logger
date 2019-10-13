from datetime import datetime
from decimal import Decimal

from flask import Blueprint, jsonify, request, g

from src.db_models.activity import Activity

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/activities', methods=['POST'])
def activities():
    api_input = request.get_json()
    if api_input.get('operation') == 'add':
        _add_activity(api_input)
    response = jsonify({})
    response.status_code = 200
    return response


def _add_activity(api_input):
    activity = Activity(
        athlete_id=api_input.get('athlete_id'),
        type=api_input.get('activity_type'),
        date=datetime.strptime(api_input.get('activity_date'), '%Y-%m-%d'),
        distance=Decimal(api_input.get('activity_distance')),
        duration=Decimal(api_input.get('activity_duration'))
    )

    g.db.session.add(activity)
    g.db.session.commit()
