import requests

url = 'http://127.0.0.1:5000/upscale/'
# with open('example/lama_300px_1.png', 'rb') as file:
#     resp = requests.post(url, files={'user_image': file})
#     print(resp.status_code)
#     print(resp.headers)
#     print(resp.text)

resp = requests.get(url+'46c5acab-2545-407a-abc1-55b2ee179ef6')
print(resp.text)
