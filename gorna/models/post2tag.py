from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class Post2Tag(Base):
    """ The SQLAlchemy declarative model class for a News object. """
    __tablename__ = 'TabPost2Tag'
    uid = Column(CHAR, primary_key=True, nullable=False)
    par_id = Column(CHAR, nullable=False)
    tag_id = Column(CHAR, nullable=False)
    post_id = Column(CHAR, nullable=False)
    order = Column(Integer)
