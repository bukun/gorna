from sqlalchemy import (
    Column,
    Integer,
    CHAR
)

from .meta import Base


class Link(Base):
    """ The SQLAlchemy declarative model class for a Post object. """
    __tablename__ = 'TabLink'
    uid = Column(CHAR, primary_key=True, nullable=False)
    link = Column(CHAR, nullable=False)
    name = Column(CHAR, nullable=False)
    logo = Column(CHAR, nullable=False)
    order = Column(Integer,default=0)

