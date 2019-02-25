from sqlalchemy import (
    Column,
    CHAR,
    BigInteger

)

from .meta import Base


class Log(Base):
    """ The SQLAlchemy declarative model class for Log object. """
    __tablename__ = 'TabLog'
    uid = Column(CHAR, primary_key=True, nullable=False)
    current_url = Column(CHAR, nullable=False)
    refer_url = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    time_create = Column(BigInteger)
    time_out = Column(BigInteger)
    time = Column(BigInteger)
