import requests


class YandexApi():
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_dir(self):
        path = 'Test new dir'
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.put(url, headers=headers, params=params)
        return response.status_code

    def disk_info(self):
        path = '/'
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.get(url, headers=headers, params=params)
        info = response.json()
        result = len(info['_embedded']['items'])
        return result

    def remove_dir(self):
        path = 'Test new dir'
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.delete(url, headers=headers, params=params)
        return response.status_code
