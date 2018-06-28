from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class Evaluation(Base):
    """ The SQLAlchemy declarative model class for a News object. """
    __tablename__ = 'TabEvaluation'
    uid = Column(CHAR, primary_key=True, nullable=False)
    post_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    value = Column(Integer, nullable=False)
