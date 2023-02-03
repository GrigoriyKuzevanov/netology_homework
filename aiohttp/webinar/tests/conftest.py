import time

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from models import Base, UserModel

DB_DSN = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DB_DSN)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture()
def create_adv():
    with Session() as session:
        new_user = UserModel(username=f"user_{time.time()}", password="1234")
        session.add(new_user)
        session.commit()
        return {
            "id": new_user.id,
            "username": new_user.username,
            "password": new_user.password,
        }
