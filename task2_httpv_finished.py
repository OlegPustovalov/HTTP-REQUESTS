import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, disk_file_path: str, filename: str):
        """Метод загружает файл на яндекс диск"""
        #выделяем место на яндекс диске
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        #в заголовке авторизация с токеном
        headers = {"Authorization": self.token}
        #disk_file_path в параметрах указывается путь на яндекс диске куда надо записать файл
        #overwrite = true для возможности перезаписи файла, если тот существует
        params = {"path":disk_file_path,"overwrite":"true"}
        response = requests.get(upload_url,headers = headers,params = params)
        #проверка статуса http запроса
        res = response.status_code
        print (res)
        #считывание данных с яндекс диска в виде словаря
        response_href = response.json()
        print (response_href)
        #поиск в этом словаре параметра href ссылки
        Url = response_href.get("href")
        print (Url)
        print(filename)
        #запись файла filename на выделенное яндекс диск место по disk_file_path
        with open(filename,'rb',) as file1:
             files = {'file': file1}
             response = requests.put(Url, files=files, headers=headers)
                
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    #имя загружаемого файла
    #путь вместе с новым названием файла на яндекс диске
    path_to_file = "file_yadisk.txt"
    filename = "file_local_disk.txt"
    # токен к OlegPolygon
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, filename)