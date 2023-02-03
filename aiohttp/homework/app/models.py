from sqlalchemy import Column, Integer, String, Text, func, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class AdvModel(Base):

    __tablename__ = 'advs'

    id = Column(Integer, primary_key=True)
    header = Column(String(42), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    creation_date = Column(DateTime, server_default=func.now())
    owner = Column(String(32), nullable=False)
