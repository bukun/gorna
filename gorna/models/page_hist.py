from sqlalchemy import (
    Column,
    Integer,
    CHAR,
    Text
)

from .meta import Base


class PageHist(Base):
    """ The SQLAlchemy declarative model class for  PageHist object. """
    __tablename__ = 'TabWikiHist'
    uid = Column(CHAR, primary_key=True, nullable=False)
    title = Column(CHAR, nullable=False)
    wiki_id = Column(CHAR, nullable=False)
    user_name = Column(CHAR)
    cnt_md = Column(Text)
    time_update = Column(Integer)
