from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class PostModel(Base):
    """ The SQLAlchemy declarative model class for a Post object. """
    __tablename__ = 'tabpost'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    cnt_md = Column(Text, nullable=False)
    cnt_html = Column(Text, nullable=False)
