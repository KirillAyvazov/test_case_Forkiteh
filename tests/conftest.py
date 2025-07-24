import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Text, UUID
from fastapi.testclient import TestClient

from repository.repo import Repository
from app import app


@pytest.fixture(scope="session")
def base_fixture():
    Base = declarative_base()
    return Base


@pytest.fixture(scope="session")
def model_fixture(base_fixture):
    class InfoModel(base_fixture):
        __tablename__ = 'info'
        id = Column(UUID, primary_key=True)
        address = Column(Text, nullable=True)
        bandwidth = Column(Integer, nullable=True)
        energy = Column(Integer, nullable=True)
        trx = Column(Integer, nullable=True)
        date_time = Column(DateTime, nullable=False, default=datetime.utcnow)

    return InfoModel


@pytest.fixture(scope="session")
def session_db_fixture(base_fixture):
    engine = create_engine('sqlite:///info.db')
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    base_fixture.metadata.create_all(engine)

    return session


@pytest.fixture(scope="session")
def method_write_in_db():
    repo = Repository()
    method = getattr(repo, "_write_in_db")
    return method


@pytest.fixture(scope="session")
def test_client():
    return TestClient(app)
