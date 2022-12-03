import requests


def get_intelligence(name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    resp = requests.get(url)
    info = resp.json()
    intelligence = int(info['results'][0]['powerstats']['intelligence'])
    return intelligence


def the_most_intelligence(names):
    count = 0
    for name in names:
        if get_intelligence(name) > count:
            result = f'Самый умный герой {name}, его интеллект: {get_intelligence(name)}'
            count = get_intelligence(name)
    print(result)


the_most_intelligence(['Hulk', 'Captain America', 'Thanos'])
