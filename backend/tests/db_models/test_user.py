from unittest import TestCase

from db_models.user import User, UserType, engine, Base
from src import db


class TestUserModel(TestCase):
    def setUp(self):
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_can_save_a_user_and_retrieve_values_and_properties(self):
        user = User(
            first_name='Thor',
            last_name='Ragnarok',
            type='athlete'
        )
        db.session.add(user)
        db.session.commit()

        all_users = db.session.query(User).all()
        self.assertEqual(1, len(all_users))
        self.assertEqual('Thor', user.first_name)
        self.assertEqual('Ragnarok', user.last_name)
        self.assertEqual(UserType.athlete.value, user.type)

        self.assertEqual('Thor Ragnarok', user.name)
