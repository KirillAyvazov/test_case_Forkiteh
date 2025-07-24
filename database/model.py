from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, Text, UUID


Base = declarative_base()


class InfoModel(Base):
    __tablename__ = 'info'
    id = Column(UUID, primary_key=True)
    address = Column(Text, nullable=True)
    bandwidth = Column(Integer, nullable=True)
    energy = Column(Integer, nullable=True)
    trx = Column(Integer, nullable=True)
    date_time = Column(DateTime, nullable=False, default=datetime.utcnow)
