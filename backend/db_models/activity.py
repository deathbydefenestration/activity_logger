from enum import Enum as PythonEnum

from sqlalchemy import Column, Integer, create_engine, ForeignKey, DECIMAL, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import config
from db_models.athlete import Athlete

Base = declarative_base()


class ActivityType(PythonEnum):
    run = 'run'
    swim = 'swim'


class Activity(Base):
    """
    Activity Model

    The record for an Athlete's exercise log. An Athlete would be able to log different types of Activity, i.e. run or
    swim.

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


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)
