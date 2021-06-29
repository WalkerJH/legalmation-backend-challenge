import main
import requests
import sqlite3

input_folder = 'test_input/'
local_host_url = 'http://127.0.0.1:5000/'

def test_file_upload():
    f = open(input_folder + 'A.xml', 'rb')
    files = {'file': f}
    requests.post(local_host_url, files = files)
    f.close()

def test_api_response():
    f = open(input_folder + 'A.xml', 'rb')
    files = {'file': f}
    r = requests.post(local_host_url, files = files)
    f.close()
    assert(r.text is not None)
    
def test_api_response_json():
    f = open(input_folder + 'A.xml', 'rb')
    files = {'file': f}
    r = requests.post(local_host_url, files = files)
    f.close()
    assert('ANGELO ANGELES' in str(r.text) and 'HILL-ROM COMPANY, INC.' in str(r.text))

def test_db_connect():
    conn = sqlite3.connect('complaints.db')
    c = conn.cursor()
    conn.close()

def test_db_add_and_retrieve():
    complaint_dict = {'filename': 'testfile', 'plaintiffs': 'Kim Plaintiff', 'defendants': 'Greed Inc'}
    main.add_db_entry(complaint_dict)
    assert(main.retrieve_db_entry('testfile') == complaint_dict)
