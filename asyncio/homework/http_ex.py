import requests
from pprint import pprint

response = requests.get('https://swapi.dev/api/people/').json()

# count = response['count']

for i in range(20, 21):
    response = requests.get(f'https://swapi.dev/api/people/{i}').json()
    pprint(response)
    print('=============================================================')
    # print(type(response['homeworld']))
    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    