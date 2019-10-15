from datetime import date
from decimal import Decimal
from unittest import TestCase

from flask import json, g

from src.db_models.activity import Base as ActivityBase, Activity, ActivityType
from src.db_models.athlete import engine, Base as AthleteBase, Athlete
from src.db_models.user import User, Base as UserBase

from src import create_app


class TestAPI(TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        UserBase.metadata.create_all(engine)
        AthleteBase.metadata.create_all(engine)
        ActivityBase.metadata.create_all(engine)

        self.user = User(
            first_name='Dina',
            last_name='Asher-Smith',
            type='athlete'
        )
        g.db.session.add(self.user)
        g.db.session.commit()

        self.athlete = Athlete(
            user_id=self.user.id,
            weight=Decimal('57.83')
        )
        g.db.session.add(self.athlete)
        g.db.session.commit()

        self.headers = {'content-type': 'application/json'}

        self.payload = {
            'athlete_id': self.athlete.id,
            'operation': 'add',
            'activity_type': 'run',
            'activity_date': '2019-09-27',
            'activity_distance': '100',
            'activity_duration': '10.83'
        }
        self.data = json.dumps(self.payload)

    def tearDown(self):
        AthleteBase.metadata.drop_all(engine)
        UserBase.metadata.drop_all(engine)
        ActivityBase.metadata.drop_all(engine)

    def test_activities_api_can_add_an_activity(self):
        response = self.client().post(
            '/api/activities', data=self.data, headers=self.headers
        )
        self.assertEqual(response.status_code, 200)

        all_activities = g.db.session.query(Activity).all()
        self.assertEqual(1, len(all_activities))

        activity = all_activities[0]
        self.assertEqual(self.athlete.id, activity.athlete_id)
        self.assertEqual(ActivityType.run.value, activity.type)
        self.assertEqual(date(year=2019, month=9, day=27), activity.date)
        self.assertEqual(Decimal('100.00'), activity.distance)
        self.assertEqual(Decimal('10.83'), activity.duration)

    def test_activities_api_returns_error_for_incomplete_activity(self):
        payload = {
            'athlete_id': self.athlete.id,
            'operation': 'add',
        }

        response = self.client().post(
            '/api/activities', data=json.dumps(payload), headers=self.headers
        )

        all_activities = g.db.session.query(Activity).all()
        self.assertEqual(0, len(all_activities))

        response_json = response.get_json()
        self.assertIsNotNone(response_json['error'])
        self.assertEqual(400, response.status_code)

    def test_activities_api_returns_the_activity_as_json_if_successful(self):
        response = self.client().post(
            '/api/activities', data=self.data, headers=self.headers
        )
        self.assertEqual(response.status_code, 200)

        response_json = response.get_json()
        expected_number_of_results = 1
        self.assertEqual(expected_number_of_results, len(response_json))

        result = response_json[0]
        self.assertEqual(str(self.athlete.id), result['athlete_id'])
        self.assertEqual('2019-09-27', result['date'])
        self.assertEqual('100.00', result['distance'])
        self.assertEqual('10.83', result['duration'])
        self.assertEqual('run', result['type'])
        self.assertEqual('50.191', result['calories_burned'])
