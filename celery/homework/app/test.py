import requests

url = 'http://localhost:5000/upscale/'
with open('example/lama_300px_1.png', 'rb') as file:
    resp = requests.post(url, files={'user_image': file})
    print(resp.status_code)
    print(resp.headers)
    print(resp.text)

# resp = requests.get(url+'')
# print(resp.text)
