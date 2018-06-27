from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class News(Base):
    """ The SQLAlchemy declarative model class for a News object. """
    __tablename__ = 'news'
    uid = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, unique=True)
    content = Column(Text, nullable=False)
    time_create = Column(Text, nullable=False)
    time_update = Column(Text, nullable=False)