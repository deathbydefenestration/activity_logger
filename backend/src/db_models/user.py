from enum import Enum as PythonEnum

from sqlalchemy import Column, Integer, String, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

import config

Base = declarative_base()


class UserType(PythonEnum):
    athlete = 'athlete'
    coach = 'coach'


class User(Base):
    """
    User Model

    The standard system user. Users can be distinguished by their types, i.e. an athlete or a coach.

    For the purposes of this exercise, usual fields like email address and password are not included: no login system
    is being built.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    first_name = Column(String(50))

    last_name = Column(String(50))

    type = Column(
        Enum(
            UserType.athlete.value,
            UserType.coach.value
        )
    )

    @hybrid_property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)
