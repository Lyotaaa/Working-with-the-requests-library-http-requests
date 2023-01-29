import requests
from pprint import pprint

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, path_to_file):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()
    
    def upload_file_to_disk(sefl, path_to_file, file_name):
        result = sefl._get_upload_link(path_to_file=path_to_file)
        url = result.get('href')
        respons = requests.put(url, data=open(file_name, 'rb'))
        respons.raise_for_status
        # if respons.status_code == 201:
        #     print('Success')

if __name__ == '__main__':
    path_to_file = '!/test.txt'
    token = ''
    file_name = 'text.txt'
    uploader = YandexDisk(token=token)
    res = uploader.upload_file_to_disk(path_to_file, file_name)
    if res == None:
        print(f'Файл загружен')