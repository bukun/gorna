from sqlalchemy import (
    Column,
    Integer,
    CHAR,
    Float

)

from .meta import Base


class Rel(Base):
    """ The SQLAlchemy declarative model class for a News object. """
    __tablename__ = 'TabRel'
    uid = Column(CHAR, primary_key=True, nullable=False)
    post_f_id = Column(CHAR, nullable=False)
    post_t_id = Column(CHAR, nullable=False)
    count = Column(Integer, nullable=False)
