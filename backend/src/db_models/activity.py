from decimal import Decimal
from enum import Enum as PythonEnum

from sqlalchemy import Column, Integer, create_engine, ForeignKey, DECIMAL, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import config
from src.db_models.athlete import Athlete

Base = declarative_base()

RESPIRATORY_EXCHANGE_RATIO = Decimal(4.86)
LEGER_EQUATION_CONSTANT = Decimal(2.209) + Decimal(3.1633)
CALORIES_BURNED_DECIMAL_PLACES = 3


class ActivityType(PythonEnum):
    run = 'run'
    swim = 'swim'


class Activity(Base):
    """
    Activity Model

    The record for an Athlete's exercise log. An Athlete would be able to log different types of Activity, i.e. run or
    swim.

    Calories Burned is calculated on demand as a property, not stored, should an improved formula be used.

    """

    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)

    athlete_id = Column(Integer, ForeignKey(Athlete.id), nullable=False)

    athlete = relationship(
        Athlete, primaryjoin=athlete_id == Athlete.id, backref='athlete_activity'
    )

    type = Column(
        Enum(
            ActivityType.run.value,
            ActivityType.swim.value,
        ),
        default=ActivityType.run.value
    )

    date = Column(Date, nullable=False)

    # distance travelled in metres
    distance = Column(DECIMAL(10, 2), nullable=False)

    # duration of the activity in seconds
    duration = Column(DECIMAL(10, 2), nullable=False)

    @property
    def calories_burned(self):
        kph = self.__convert_metres_per_second_to_kph(self.duration, self.distance)
        vo2 = self.__calculate_vo2_(kph)
        calories_burned = RESPIRATORY_EXCHANGE_RATIO * self.athlete.weight * vo2 / 1000
        return round(calories_burned, CALORIES_BURNED_DECIMAL_PLACES)

    @staticmethod
    def __convert_metres_per_second_to_kph(seconds, metres):
        hour = seconds / 60 / 60
        kilometres = metres / 1000
        return kilometres / hour

    @staticmethod
    def __calculate_vo2_(kph):
        return LEGER_EQUATION_CONSTANT * kph


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)
