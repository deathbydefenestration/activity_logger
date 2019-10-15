from datetime import date
from decimal import Decimal
from unittest import TestCase

from flask import g

from src import create_app
from src.db_models.activity import Base as ActivityBase, Activity
from src.db_models.athlete import engine, Base as AthleteBase, Athlete
from src.db_models.user import User, Base as UserBase
from src.repositories.activity_repository import ActivityRepository


class TestActivityRepository(TestCase):

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

        self.activity_repository = ActivityRepository()

        self.expected_date = date(year=2019, month=10, day=2)
        self.expected_distance = Decimal('200')
        self.expected_duration = Decimal('21.88')

    def tearDown(self):
        AthleteBase.metadata.drop_all(engine)
        UserBase.metadata.drop_all(engine)
        ActivityBase.metadata.drop_all(engine)

    def test_activity_repository_can_add_an_activity(self):
        self.activity_repository.add(
            athlete_id=self.athlete.id,
            type='run',
            date=self.expected_date,
            distance=self.expected_distance,
            duration=self.expected_duration
        )

        all_activities = g.db.session.query(Activity).all()
        self.assertEqual(1, len(all_activities))

    def test_activity_repository_can_retrieve_all_activities_by_athlete_id(self):
        number_of_expected_results = 5
        self.__add_number_of_activities(number_of_expected_results)
        results = self.activity_repository.fetch_all_activities_by_athlete_id(self.athlete.id)

        self.assertEqual(number_of_expected_results, len(results))

    def __add_number_of_activities(self, number=1):
        for i in range(number):
            self.activity_repository.add(
                athlete_id=self.athlete.id,
                type='run',
                date=self.expected_date,
                distance=self.expected_distance,
                duration=self.expected_duration
            )