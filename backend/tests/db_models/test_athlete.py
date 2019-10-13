from decimal import Decimal
from unittest import TestCase

from src.db_models.athlete import engine, Base as AthleteBase, Athlete
from src.db_models.user import User, Base as UserBase
from src import db


class TestAthleteModel(TestCase):
    def setUp(self):
        UserBase.metadata.create_all(engine)
        AthleteBase.metadata.create_all(engine)

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

    def test_can_save_an_athlete_and_return_all_values(self):
        all_athletes = db.session.query(Athlete).all()
        self.assertEqual(1, len(all_athletes))

        self.assertEqual(1, self.athlete.id)
        self.assertEqual(Decimal('57.83'), self.athlete.weight)
        self.assertEqual(self.user, self.athlete.user)
