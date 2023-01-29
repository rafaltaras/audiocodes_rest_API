import datetime, os, base64, configparser, requests
from docx import Document
from docx.shared import Inches

class Config:
    def __init__(self):
        pass

    def ensure_path(self, folderpath):   
        if os.path.exists(folderpath) is not True:
            try:
                os.mkdir(folderpath)
            except OSError:
                print(f"Creation file filed {folderpath}")
            else:
                print(f"File created {folderpath}")
        return folderpath

    def make_filepath(self, ip, folderpath):
        dt = str(datetime.datetime.now())
        filepath = folderpath + ip + "_" + dt[:10] 
        return filepath
    
    def get_url_ini_file(self, ip):
        url = f'http://{ip}/api/v1/files/ini'
        return url

    def credential(self, username, password, url):
        cred = username + ':' + password
        cred_encoded = base64.b64encode(cred.encode()).decode()
        headers = {'Authorization': 'Basic ' + cred_encoded} 
        return requests.get(url, headers=headers)

    def download_config(self, ip, username, password):
        folderpath = self.ensure_path("./backups/")        
        filepath = self.make_filepath(ip, folderpath)
        url = self.get_url_ini_file(ip)
        response = self.credential(username, password, url)
        if response.status_code != 200:
            print("Backup filed: ", response.status_code)
            return None
        filepath = filepath + ".ini"
        with open(filepath, "w") as f:
            f.write(response.text)
        return filepath

    def read_ini(self, path): 
        config = configparser.ConfigParser()
        config.sections()
        config.read(path)
        return config

    def read_parameter_details(self, path, section):
        config = self.read_ini(path)
        return config[section]

    def create_docx_file(self, ip):
        document = Document()
        folderpath = self.ensure_path("./backups/")        
        filepath = self.make_filepath(ip, folderpath)
        document.save(f'{filepath}'+'.docx')
        return None

config  = Config()
