from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class Entity2User(Base):
    """ The SQLAlchemy declarative model class for  Entity2User object. """
    __tablename__ = 'TabEntity2User'
    uid = Column(CHAR, primary_key=True, nullable=False)
    entity_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    count = Column(Integer, default=0)
    timestamp = Column(Integer, nullable=False)
