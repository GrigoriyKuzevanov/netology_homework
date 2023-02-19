import requests

url = 'http://127.0.0.1:5000/upscale/'
# with open('example/lama_300px_1.png', 'rb') as file:
#     resp = requests.post(url, files={'user_image': file})
#     print(resp.status_code)
#     print(resp.headers)
#     print(resp.text)

resp = requests.get(url+'614f820a-5472-4ca4-b140-2345dadf3182')
print(resp.text)
