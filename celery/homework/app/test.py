import requests

url = 'http://127.0.0.1:5000/upscale/'
# with open('example/lama_300px.png', 'rb') as file:
#     resp = requests.post(url, files={'user_image': file})
#     print(resp.status_code)
#     print(resp.headers)
#     print(resp.text)

resp = requests.get(url+'2f5b2879-78ba-4f7d-bba3-2f2aac918b18')
print(resp.text)
