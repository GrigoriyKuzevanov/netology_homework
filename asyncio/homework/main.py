import asyncio
import requests
import datetime
from pprint import pprint
from aiohttp import ClientSession
from more_itertools import chunked


def get_key(d, value):
    for key, val in d.items():
        if val == value:
            return key


def get_count(url):
    response = requests.get(url).json()
    return response['count']


##############################################################
async def get_info(url, session):
    async with session.get(url) as response:
        data = await response.json()
        if 'name' in data:
            return data['name']
        if 'title' in data:
            return data['title']
    

###########################################11111111111111111111111111111111#########################################
# async def json_handler(ob):
#     async with ClientSession() as session:
#         if isinstance(ob, str):
#             task = asyncio.create_task(get_info(url=ob, session=session))
#             await task
#             return task.result()
#         elif isinstance(ob, list):
#             tasks = []
#             for item in ob:
#                 task = asyncio.create_task(get_info(url=item, session=session))
#                 tasks.append(task)
#             results = await asyncio.gather(*tasks)
#             return ', '.join(results)



# ###########################################11111111111111111111111111111111#########################################
# async def get_person(id, session):
#     async with session.get(f'{URL}{id}') as response:
#         data = await response.json()
#         try:
#             data['id'] = id
#             data['homeworld'] = await json_handler(data['homeworld'])
#             data['films'] = await json_handler(data['films'])
#             data['species'] = await json_handler(data['species'])
#             data['starships'] = await json_handler(data['starships'])
#             data['vehicles'] = await json_handler(data['vehicles'])
#             return data
#         except KeyError:
#             pass

# async def get_person(id, session):
#     async with session.get(f'{URL}{id}') as response:
#         data = await response.json()
#         return data



##############################################################


URL = 'https://swapi.dev/api/people/'
CHUNK_SIZE = 10


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


############################################222222222222222222222222222222222#########################################
async def json_handler(obj):
    async with ClientSession() as session:
        if isinstance(obj, str):
            task = asyncio.create_task(get_info(url=obj, session=session))
            await task
            return {task.result(): obj}
        elif isinstance(obj, list):
            tasks = []
            for item in obj:
                task = asyncio.create_task(get_info(url=item, session=session))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            return {', '.join(results): obj}


############################################222222222222222222222222222222222#########################################
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
            tasks = [json_handler(data[key]) for key in keys]
            results = await asyncio.gather(*tasks)
            data['id'] = id
            for key in data:
                for result in results:
                    if data[key] in result.values():
                        data[key] = get_key(result, data[key])
            return data
        except KeyError:
            pass




# ############################################222222222222222222222222222222222#########################################
async def get_people():
    count = get_count(URL) + 1
    async with ClientSession() as session:
        for chunk in chunked(range(1, count), CHUNK_SIZE):
            coroutines = [get_person(id=i, session=session) for i in chunk]
            results = await asyncio.gather(*coroutines)
            for result in results:
                if result:
                    yield result


async def print_people(chunk):
    pprint(chunk)


async def main():
    async for chunk in chunked_async(CHUNK_SIZE, get_people()):
        asyncio.create_task(print_people(chunk))
    
    tasks = set(asyncio.all_tasks()) - {asyncio.current_task()}
    for task in tasks:
        await task


start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
