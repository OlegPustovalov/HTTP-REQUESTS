import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, disk_file_path: str, filename: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": self.token}
        params = {"path":disk_file_path,"overwrite":"true"}
        response = requests.get(upload_url,headers = headers,params = params)
        res = response.status_code
        print (res)
        response_href = response.json()
        print (response_href)
        Url = response_href.get("href")
        print (Url)
        print(filename)
        #do not put!!!
        response = requests.put(Url,data = (filename,'rb'))
        
if __name__ == '__main__':
    
    path_to_file = "file_yadisk.txt"
    filename = "file_local_disk.txt"
    token = ....
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, filename)