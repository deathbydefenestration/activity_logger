from sqlalchemy import Column, Integer, create_engine, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import config
from src.db_models.user import User

Base = declarative_base()


class Athlete(Base):
    """
    Athlete Model

    An Athlete record for a system User. These attributes pertain only to Athletes, i.e. weight (in kg)

    """

    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey(User.id), unique=True)

    user = relationship(
        User, primaryjoin=user_id == User.id, backref='athlete_user'
    )

    # Weight in kg
    weight = Column(DECIMAL(5, 2))


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)
