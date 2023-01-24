import asyncio
from pprint import pprint
from aiohttp import ClientSession


async def get_info(url, session):
    async with session.get(url) as response:
        data = await response.json()
        if 'name' in data:
            return data['name']
        if 'title' in data:
            return data['title']
    

async def main(ob):
    async with ClientSession() as session:
        if isinstance(ob, str) and ob == '':
            return 'unknown'
        elif isinstance(ob, str):
            task = asyncio.create_task(get_info(url=ob, session=session))
            await task
            return task.result()
        elif isinstance(ob, list):
            tasks = []
            for item in ob:
                task = asyncio.create_task(get_info(url=item, session=session))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            return ', '.join(results)


es = ''
l = []
a = ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/']
s = 'https://swapi.dev/api/planets/14/'

print(asyncio.run(main(es)))

