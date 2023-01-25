import asyncio
import requests
import datetime
from pprint import pprint
from aiohttp import ClientSession
from more_itertools import chunked
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text


URL = 'https://swapi.dev/api/people/'
CHUNK_SIZE = 20

###########################################################################
PG_DSN = 'postgresql+asyncpg://test_user:test_password@127.0.0.1:5431/test_db'
engine = create_async_engine(PG_DSN)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class People(Base):

    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    name = Column(String, nullable=False)
    gender = Column(String(30))
    birth_year = Column(String(30))
    homeworld = Column(String(50))
    height = Column(String(30))
    mass = Column(String(30))
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    species = Column(String(200))
    starships = Column(String(200))
    vehicles = Column(String(200))
    films = Column(String(200))

###########################################################################


# Вспомогательные функции получения количества
# доступных персонажей и получения ключа словаря по значению
def get_key(d, value):
    for key, val in d.items():
        if val == value:
            return key


def get_count(url):
    response = requests.get(url).json()
    return response['count']


# получене названий планет, фильмов, кораблей, транспортных средств и видов
async def get_info(url, session):
    async with session.get(url) as response:
        data = await response.json()
        if 'name' in data:
            return data['name']
        if 'title' in data:
            return data['title']


# генератор для асинхронного запуска
async def chunked_async(size, async_iter):
    buffer = []
    while True:
        try:
            item = await async_iter.__anext__()
        except StopAsyncIteration:
            break
        buffer.append(item)
        if len(buffer) == size:
            yield buffer
            buffer = []


# Обработчик объекта - строки или списка строк
async def obj_handler(obj):
    async with ClientSession() as session:
        if isinstance(obj, str) and obj:
            task = asyncio.create_task(get_info(url=obj, session=session))
            await task
            return {task.result(): obj}
        elif isinstance(obj, str) and not obj:
            return {'unknown': obj}
        elif isinstance(obj, list) and obj:
            tasks = []
            for item in obj:
                task = asyncio.create_task(get_info(url=item, session=session))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            return {', '.join(results): obj}
        elif isinstance(obj, list) and not obj:
            return {'unknown': obj}


# Получение данных по id персонажа, преобразование данных в требуемый вид
async def get_person(id, session):
    async with session.get(f'{URL}{id}') as response:
        data = await response.json()
        keys = [
            'homeworld',
            'films',
            'species',
            'starships',
            'vehicles',
        ]
        try:
            tasks = [obj_handler(data[key]) for key in keys]
            results = await asyncio.gather(*tasks)
            data['id'] = id
            for key in data:
                for result in results:
                    if data[key] in result.values():
                        data[key] = get_key(result, data[key])
            return data
        except KeyError:
            pass


# Получение данных по персонажам
async def get_people():
    count = get_count(URL) + 1
    async with ClientSession() as session:
        for chunk in chunked(range(1, count), CHUNK_SIZE):
            coroutines = [get_person(id=i, session=session) for i in chunk]
            results = await asyncio.gather(*coroutines)
            for result in results:
                if result:
                    yield result


# # Временная функция вывода в консоль
# async def print_people(chunk):
#     for c in chunk:
#         print(c['id'])
#         print(c['name'])
#         print(c['gender'])
#         print(c['birth_year'])
#         print(c['homeworld'])
#         print(c['eye_color'])
#         print(c['hair_color'])
#         print(c['skin_color'])
#         print(c['height'])
#         print(c['films'])
#         print(c['species'])
#         print(c['starships'])
#         print(c['vehicles'])
#         print('=================================================')


# Функция передачи данных в базу
async def insert_people(chunk):
    async with Session() as session:
        people = []
        for item in chunk:
            person = People(
                person_id=item['id'],
                name=item['name'],
                gender=item['gender'],
                birth_year=item['birth_year'],
                homeworld=item['homeworld'],
                height=item['height'],
                mass=item['mass'],
                hair_color=item['hair_color'],
                skin_color=item['skin_color'],
                starships=item['starships'],
                vehicles=item['vehicles'],
                films=item['films'],
            )
            people.append(person)
        session.add_all(people)
        await session.commit()


# async def main():
#     async for chunk in chunked_async(CHUNK_SIZE, get_people()):
#         asyncio.create_task(print_people(chunk))
    
#     tasks = set(asyncio.all_tasks()) - {asyncio.current_task()}
#     for task in tasks:
#         await task

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    async for chunk in chunked_async(CHUNK_SIZE, get_people()):
        asyncio.create_task(insert_people(chunk))
    
    tasks = set(asyncio.all_tasks()) - {asyncio.current_task()}
    for task in tasks:
        await task


start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
