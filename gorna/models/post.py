from sqlalchemy import (
    Column,
    Integer,
    Text,
    CHAR,
    DateTime,
    Float

)

from .meta import Base


class Post(Base):
    """ The SQLAlchemy declarative model class for  Post object. """
    __tablename__ = 'TabPost'
    uid = Column(CHAR, primary_key=True, nullable=False)
    title = Column(CHAR, nullable=False, unique=True)
    keywords = Column(CHAR, nullable=False)
    date = Column(DateTime, nullable=False)
    time_create = Column(Integer)
    user_name = Column(CHAR, nullable=False)
    time_update = Column(Integer)
    view_count = Column(Integer)
    logo = Column(CHAR)
    order = Column(CHAR, nullable=False)
    valid = Column(Integer, nullable=False, default=1)
    cnt_md = Column(Text)
    cnt_html = Column(Text)
    kind = Column(CHAR, nullable=False, default='1')
    rating = Column(Float, nullable=False, default=5)
    memo = Column(Text, nullable=False, default='')
    extinfo = Column(Text)
