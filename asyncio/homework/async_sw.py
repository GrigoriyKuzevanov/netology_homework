import requests
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DSN = 'postgresql://test_user:1234@127.0.0.1:5431/test_db'


# engine = create_engine(DSN)
# Base = declarative_base()
# Session = sessionmaker(bind=engine)


# class People(Base):

#     __tablename__ = 'people'

#     id = Column(Integer, primary_key=True)
#     birth_year = Column(String)
#     eye_color = Column(String)
#     films = Column(String)
#     gender = Column(String)
#     hair_color = Column(String)
#     height = Column(String)
#     homeworld = Column(String)
#     mass = Column(String)
#     name = Column(String)
#     skin_color = Column(String)
#     species = Column(String)
#     starships = Column(String)
#     vehicles = Column(String)
    

def get_people(person_id):
    response = requests.get(f'https://swapi.dev/api/people/{person_id}').json()
    return response

def main(count: int):
    # Base.metadata.create_all(engine)
    people = [get_people(i) for i in range(1)]
    for person in people:
        print(person['name'])

main(10)
