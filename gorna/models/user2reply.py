from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class User2Reply(Base):
    """ The SQLAlchemy declarative model class for a News object. """
    __tablename__ = 'TabUser2Reply'
    uid = Column(CHAR, primary_key=True, nullable=False)
    reply_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    timestamp = Column(Integer, nullable=False)
