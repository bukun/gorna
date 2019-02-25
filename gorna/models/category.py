# -*- coding:utf-8 -*-



from sqlalchemy import (
    Column,
    Integer,
    CHAR

)

from .meta import Base


class Category(Base):
    """ The SQLAlchemy declarative model class for  Category object. """
    __tablename__ = 'TabTag'
    uid = Column(CHAR, primary_key=True, nullable=False)
    slug = Column(CHAR, nullable=False)
    name = Column(CHAR, nullable=False)
    order = Column(Integer)
    count = Column(Integer, default=0)
    kind = Column(CHAR, nullable=False, default='z')
    pid = Column(CHAR, nullable=False,default='xxxx')
    tmpl = Column(Integer, nullable=False, default='9')
