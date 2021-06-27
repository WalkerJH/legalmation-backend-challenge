import flask_app
import requests

input_folder = '../input/'
local_host_url = 'http://127.0.0.1:5000/'

def test_file_upload():
    files = {'file': open(input_folder + 'A.xml', 'rb')}
    r = requests.post(local_host_url, files = files)