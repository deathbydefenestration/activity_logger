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
        athlete_id = api_input.get('athlete_id')
        activity = Activity(
            athlete_id=athlete_id,
            type=api_input.get('activity_type'),
            date=datetime.strptime(api_input.get('activity_date'), '%Y-%m-%d'),
            distance=Decimal(api_input.get('activity_distance')),
            duration=Decimal(api_input.get('activity_duration'))
        )
        g.db.session.add(activity)
        g.db.session.commit()

        activities_for_athlete = g.db.session.query(Activity).filter_by(athlete_id=athlete_id).all()
        response_json = _serialise_model_query_into_json(data_list=activities_for_athlete)
        return _api_success(response_json)

    except Exception as e:
        return _api_error(error_message=str(e))


def _api_success(response_json=None, code=200):
    response = response_json
    response.status_code = code
    return response


def _api_error(error_message, error_code=400):
    response = jsonify({'error': error_message})
    response.status_code = error_code
    return response


def _serialise_model_query_into_json(data_list):
    results_list = []
    for db_model in data_list:
        fields = {}
        for field, value in db_model.__dict__.items():
            if __is_a_field_in_db_model(field):
                fields[field] = str(value)
        results_list.append(fields)
    return jsonify(results_list)


def __is_a_field_in_db_model(field):
    return not field.startswith('_') and not field.endswith('_') and field != 'metadata'