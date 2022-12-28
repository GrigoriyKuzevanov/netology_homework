import threading
import requests
import datetime
from concurrent.futures import ThreadPoolExecutor


def get_people(people_id):
    return requests.get(f'https://swapi.dev/api/people/{people_id}').json()

def main():
    with ThreadPoolExecutor(max_workers=4) as pool:
        result = pool.map(get_people, range(1, 11))
    print(list(result))

start = datetime.datetime.now()
main()
print(datetime.datetime.now() - start)
