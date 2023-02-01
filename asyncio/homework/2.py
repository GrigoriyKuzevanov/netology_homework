import asyncio
import requests
import datetime
from pprint import pprint
from aiohttp import ClientSession
from more_itertools import chunked


URL = 'https://swapi.dev/api/people/'
CHUNK_SIZE = 10


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
        if isinstance(obj, str):
            task = asyncio.create_task(get_info(url=obj, session=session))
            await task
            return task.result()
        elif isinstance(obj, list):
            tasks = []
            for item in obj:
                task = asyncio.create_task(get_info(url=item, session=session))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            return ', '.join(results)


# Получение данных по id персонажа, преобразование данных в требуемый вид
async def get_person(id, session):
    async with session.get(f'{URL}{id}') as response:
        data = await response.json()
        try:
            data['id'] = id
            data['homeworld'] = await obj_handler(data['homeworld'])
            data['films'] = await obj_handler(data['films'])
            data['species'] = await obj_handler(data['species'])
            data['starships'] = await obj_handler(data['starships'])
            data['vehicles'] = await obj_handler(data['vehicles'])
            return data
        except KeyError:
            pass

async def get_person(id, session):
    async with session.get(f'{URL}{id}') as response:
        data = await response.json()
        return data


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


# Временная функция вывода в консоль
async def print_people(chunk):
    for c in chunk:
        print(c['id'])
        print(c['name'])
        print(c['gender'])
        print(c['birth_year'])
        print(c['homeworld'])
        print(c['eye_color'])
        print(c['hair_color'])
        print(c['skin_color'])
        print(c['height'])
        print(c['films'])
        print(c['species'])
        print(c['starships'])
        print(c['vehicles'])
        # pprint(c)
        print('=================================================')


async def main():
    async for chunk in chunked_async(CHUNK_SIZE, get_people()):
        asyncio.create_task(print_people(chunk))
    
    tasks = set(asyncio.all_tasks()) - {asyncio.current_task()}
    for task in tasks:
        await task


start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
