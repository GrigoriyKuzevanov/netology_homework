import time

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tests.config import DSN
from models import Base, AdvModel


engine = create_engine(DSN)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)  #autose=True - фикстура запускается автоматически при тестах
def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@pytest.fixture()
def create_adv():
    with Session() as session:
        new_adv = AdvModel(
            header=f'header_{time.time()}',
            description='test_description',
            owner='test_owner'
        )
        session.add(new_adv)
        session.commit()
        return {
            'id': new_adv.id,
            'header': new_adv.header,
            'description': new_adv.description,
            'owner': new_adv.owner
        }
