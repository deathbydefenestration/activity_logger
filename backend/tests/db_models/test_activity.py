from datetime import date
from decimal import Decimal
from unittest import TestCase

from src.db_models.activity import Base as ActivityBase, Activity, ActivityType
from src.db_models.athlete import engine, Base as AthleteBase, Athlete
from src.db_models.user import User, Base as UserBase
from src import db


class TestActivityModel(TestCase):
    def setUp(self):
        UserBase.metadata.create_all(engine)
        AthleteBase.metadata.create_all(engine)
        ActivityBase.metadata.create_all(engine)

        self.user = User(
            first_name='Dina',
            last_name='Asher-Smith',
            type='athlete'
        )
        db.session.add(self.user)
        db.session.commit()

        self.athlete = Athlete(
            user_id=self.user.id,
            weight=Decimal('57.83')
        )
        db.session.add(self.athlete)
        db.session.commit()

    def tearDown(self):
        AthleteBase.metadata.drop_all(engine)
        UserBase.metadata.drop_all(engine)
        ActivityBase.metadata.drop_all(engine)

    def test_can_save_an_activity_and_return_all_values(self):
        expected_date = date(year=2019, month=10, day=2)
        expected_distance = Decimal('200')
        expected_duration = Decimal('21.88')

        activity = Activity(
            athlete_id=self.athlete.id,
            type='run',
            date=expected_date,
            distance=expected_distance,
            duration=expected_duration
        )
        db.session.add(activity)
        db.session.commit()

        all_activities = db.session.query(Activity).all()
        self.assertEqual(1, len(all_activities))

        # Assert Values
        self.assertEqual(self.athlete.id, activity.athlete_id)
        self.assertEqual(ActivityType.run.value, activity.type)
        self.assertEqual(expected_date, activity.date)
        self.assertEqual(expected_distance, activity.distance)
        self.assertEqual(expected_duration, activity.duration)

        # Assert Relationships
        self.assertEqual(self.athlete, activity.athlete)
        self.assertEqual(self.user, activity.athlete.user)
