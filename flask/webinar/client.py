import requests

# data = requests.post(
#     'http://127.0.0.1:5000/user/',
#     json={'name': 'user1', 'password': 'FFee5rt!rf'}
#     )
# print(data.status_code)
# print(data.text)


# data = requests.patch(
#     'http://127.0.0.1:5000/user/1',
#     json={'name': 'user1_test_patch'}
#     )
# print(data.status_code)
# print(data.text)

data = requests.delete(
    'http://127.0.0.1:5000/user/1'
    )
print(data.status_code)
print(data.text)

data = requests.get(
    'http://127.0.0.1:5000/user/1'
    )
print(data.status_code)
print(data.text)
