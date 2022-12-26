import requests


data = requests.patch('http://127.0.0.1:5000/ads/1', json={
    'header': 'Lada',
    'description': 'Lada 21101, 2007',
    'owner': 'Nastya'
    }
)
print(data.status_code)
print(data.text)
