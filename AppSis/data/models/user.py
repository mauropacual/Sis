from sqlalchemy import Column, String

from data import Base

class User(Base):
    __tablename__ = 'user'
    id_user = Column(String(4), primary_key=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable=False)