from sqlalchemy import (
    Column,
    Integer,
    CHAR,
    Text,
    DateTime
)

from .meta import Base


class Reply(Base):
    """ The SQLAlchemy declarative model class for Reply object. """
    __tablename__ = 'TabReply'
    uid = Column(CHAR, primary_key=True, nullable=False)
    post_id = Column(CHAR, nullable=False)
    user_id = Column(CHAR, nullable=False)
    user_name = Column(Text)
    timestamp = Column(Integer)
    date = Column(DateTime)
    cnt_md = Column(Text)
    cnt_html = Column(Text)
    vote = Column(Integer)
