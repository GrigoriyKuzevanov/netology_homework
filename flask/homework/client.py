import requests


data = requests.get('http://127.0.0.1:5000/ads/1')
print(data.status_code)
print(data.text)
