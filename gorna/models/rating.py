from sqlalchemy import (
    Column,
    Integer,
    CHAR,
    Float

)

from .meta import Base


class Rating(Base):
    """ The SQLAlchemy declarative model class for Rating object. """
    __tablename__ = 'TabRating'
    uid = Column(CHAR, primary_key=True, nullable=False)
    post_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    rating = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)
