import requests
import datetime
import sys
import os
import base64
import configparser

class Config:
    def __init__(self) -> None:
        pass

    def download_config(self, ip, username, password):
        folderpath = 'C:\\project\\audc_config_rest_api\\backups\\'
        if os.path.exists(folderpath) is not True:
            try:
                os.mkdir(folderpath)
            except OSError:
                print("Creation file filed" %folderpath)
            else:
                print("File created" %folderpath)
        dt = str(datetime.datetime.now())
        FilePath = folderpath + ip + "_" + dt[:10] + ".ini"
        url = f'http://{ip}/api/v1/files/ini'
        cred = username + ':' + password
        cred_encoded = base64.b64encode(cred.encode()).decode()
        headers = {'Authorization': 'Basic ' + cred_encoded}
        response = requests.get(url, headers=headers)
        response.status_code
        if (response.status_code) == 200:
            File = open(FilePath,"w")
            File.write(response.text)
            File.close()
        else:
            print("Backup filed: ", response.status_code) 
        return FilePath

    def read_ini(self, file_name): 
        config = configparser.ConfigParser()
        config.sections()
        config.read(f"C:\\project\\audc_config_rest_api\\backups\\{file_name}.ini")
        return config.sections()

config  = Config()

config.read_ini(file_name = "6.204.12.8_2023-01-24")