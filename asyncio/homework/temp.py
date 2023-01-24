import requests

def get_count():
    response = requests.get('https://swapi.dev/api/people/').json()
    return response['count']

def get_person(person_id):
    response = requests.get(f'https://swapi.dev/api/people/{person_id}').json()
    return response

def get_people():
    people = [get_person(i) for i in range(1, 10) if 'name' in get_person(i)]
    return people

def get_by_api(url):
    response = requests.get(url).json()
    if 'title' in response.keys():
        return response['title']
    else:
        return response['name']

def get_item(items):
    res = ', '.join([get_by_api(item) for item in items])
    return res

def main():
    for person in get_people():
        name = person['name']
        films = get_item(person['films'])
        homeworld = get_by_api(person['homeworld'])
        species = get_item(person['species'])
        starships = get_item(person['starships'])
        vehicles = get_item(person['vehicles'])
        print(f'Name: {name}')
        print(f'Films: {films}')
        print(f'Homeworld: {homeworld}')
        print(f'Species: {species}')
        print(f'Starships: {starships}')
        print(f'Vehicles: {vehicles}')
        print('=' * 100)
        

main()
