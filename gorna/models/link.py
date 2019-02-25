from sqlalchemy import (
    Column,
    Integer,
    CHAR
)

from .meta import Base


class Link(Base):
    """ The SQLAlchemy declarative model class for  Link object. """
    __tablename__ = 'TabLink'
    uid = Column(CHAR, primary_key=True, nullable=False,default='0000')
    link = Column(CHAR, nullable=False)
    name = Column(CHAR, nullable=False)
    logo = Column(CHAR, nullable=False)
    order = Column(Integer)
