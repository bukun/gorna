from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    CHAR,
    DateTime
)
from sqlalchemy.orm import relationship

from .meta import Base


class Page(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'TabWiki'
    uid = Column(CHAR, primary_key=True, nullable=False)
    title = Column(CHAR, nullable=False, unique=True)
    date = Column(DateTime)
    time_create = Column(Integer, nullable=True)
    user_name = Column(CHAR, nullable=False)
    time_update = Column(Integer, nullable=False)
    view_count = Column(Integer)
    cnt_md = Column(Text)
    cnt_html = Column(Text)
    kind = Column(CHAR, nullable=False, default='1')



    # creator_id = Column(ForeignKey('users.id'), nullable=False)
    # creator = relationship('User', backref='created_pages')
