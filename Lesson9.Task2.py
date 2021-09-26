from pprint import pprint
import requests


TOKEN = "..."

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, disk_file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_name, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()


    def upload(self, disk_file_name):
        """Метод загружает файл на яндекс диск"""
        href = self._get_upload_link(disk_file_name).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':

    filename = "Test_recipes.txt"
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(filename)


