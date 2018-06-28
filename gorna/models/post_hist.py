from sqlalchemy import (
    Column,
    Integer,
    CHAR,
    Text
)

from .meta import Base


class PostHist(Base):
    """ The SQLAlchemy declarative model class for a Post object. """
    __tablename__ = 'TabPostHist'
    uid = Column(CHAR, primary_key=True, nullable=False)
    title = Column(CHAR, nullable=False)
    post_id = Column(CHAR, nullable=False)
    user_name = Column(CHAR)
    cnt_md = Column(Text)
    time_update = Column(Integer)
    logo = Column(CHAR)
