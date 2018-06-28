import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    Text,
    CHAR
)

from .meta import Base


class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'TabMember'
    uid = Column(CHAR, primary_key=True, nullable=False, unique=True)
    user_name = Column(CHAR, nullable=False, unique=True)
    user_email = Column(CHAR, nullable=False, unique=True)
    user_pass = Column(CHAR, nullable=False)
    role = Column(CHAR, nullable=False)
    time_reset_passwd = Column(Integer, nullable=False, default=0)
    time_login = Column(Integer, nullable=False, default=0)
    time_create = Column(Integer, nullable=False, default=0)
    time_update = Column(Integer, nullable=False, default=0)
    time_email = Column(Integer, nullable=False, default=0)
    extinfo = Column(Text, nullable=True)



    # ----------------------------------

    password_hash = Column(Text)

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False
