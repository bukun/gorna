from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class Usage(Base):
    """ The SQLAlchemy declarative model class for Usage object. """
    __tablename__ = 'TabUsage'
    uid = Column(CHAR, primary_key=True, nullable=False)
    post_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    count = Column(Integer)
    tag_id = Column(CHAR, nullable=False)
    kind = Column(CHAR, nullable=False)
    timestamp = Column(Integer)
