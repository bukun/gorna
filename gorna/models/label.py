from sqlalchemy import (
    Column,
    Integer,
    CHAR
)

from .meta import Base


class Label(Base):
    """ The SQLAlchemy declarative model class for a Post object. """
    __tablename__ = 'TabTag'
    uid = Column(CHAR, primary_key=True, nullable=False)
    slug = Column(CHAR, nullable=False)
    name = Column(CHAR, nullable=False)
    order = Column(Integer)
    count = Column(Integer,default=0)
    kind = Column(CHAR, nullable=False,default='z')
    pid = Column(CHAR, nullable=False,default='xxxx')
    tmpl = Column(Integer, nullable=False,default='9')


class MPost2Label(Base):
    '''
    For post 2 label
    '''

    def __init__(self):
        super(MPost2Label, self).__init__()