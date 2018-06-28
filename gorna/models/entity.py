from sqlalchemy import (
    Column,
    Integer,
    CHAR
)

from .meta import Base


class Entity(Base):
    """ The SQLAlchemy declarative model class for a Post object. """
    __tablename__ = 'TabEntity'
    uid = Column(CHAR, primary_key=True, nullable=False)
    path = Column(CHAR, nullable=False, unique=True)
    desc = Column(CHAR, nullable=False)
    time_create = Column(Integer)
    kind = Column(CHAR, nullable=False, default='1')
