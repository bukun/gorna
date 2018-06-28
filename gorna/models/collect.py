from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class Collect(Base):
    """ The SQLAlchemy declarative model class for a News object. """
    __tablename__ = 'TabCollect'
    uid = Column(CHAR, primary_key=True, nullable=False)
    post_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    timestamp = Column(Integer, nullable=False)
