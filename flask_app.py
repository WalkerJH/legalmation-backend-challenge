"""Flask app to parse plaintiffs and defendants from legal complaint"""
__author__      = "Walker Herring"

from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
import os
import complaint_parser
import sqlite3
import json

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

ABBYY_NS_STR = 'http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml'

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 4
app.config['UPLOAD_EXTENSIONS'] = ['.xml']

@app.route('/', methods = ['GET', 'POST'])
def mainpage():
    r = render_template('mainpage.html')
    if request.method == 'POST':
        file = request.files['file']
        if (validate_file(file)):
            r = process_xml(file)
    return r

@app.errorhandler(400)
def error(message):
    return render_template('error.html', text=message)

def validate_file(file):
    filename = file.filename
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400, "File is not xml")
    
    contents = str(file.read())
    file.seek(0, 0)
    if ABBYY_NS_STR not in contents:
        abort(400, "File not created with FineReader")

    return True

def process_xml(file):
    complaint_dict = {}
    complaint_dict['filename'] = file.filename
    filetext = file.read().decode('utf-8')
    complaint_dict['defendants'] = complaint_parser.get_defendants_from_xml(filetext)
    complaint_dict['plaintiffs'] = complaint_parser.get_plaintiffs_from_xml(filetext)
    complaint_json = json.dumps(complaint_dict, indent=4)
    
    add_db_entry(complaint_dict)

    return complaint_json

def add_db_entry(complaint_dict):
    try:
        conn = sqlite3.connect('complaints.db')
        cursor = conn.cursor()
        insert_query = "REPLACE INTO COMPLAINTS(FILENAME, DEFENDANTS, PLAINTIFFS) VALUES (?, ?, ?)"
        data = (complaint_dict['filename'], complaint_dict['defendants'], complaint_dict['plaintiffs'])
        cursor.execute(insert_query, data)
        conn.commit()
    except sqlite3.Error as e: 
        print(e)
        abort(500, 'Database error')
    finally:
        conn.close()

def retrieve_db_entry(filename):
    dict = {}
    dict['filename'] = filename
    try:
        conn = sqlite3.connect('complaints.db')
        cursor = conn.cursor()
        insert_query = "SELECT * FROM COMPLAINTS WHERE FILENAME=?;"
        cursor.execute(insert_query, [filename])
        row = cursor.fetchone()
        dict['defendants'] = row[1]
        dict['plaintiffs'] = row[2]
    except sqlite3.Error as e: 
        print(e)
        abort(500, 'Database error')
    finally:
        conn.close()
        return dict

def initialize_db():
    try:
        conn = sqlite3.connect('complaints.db')
        cursor = conn.cursor()
        create_query = 'CREATE TABLE IF NOT EXISTS COMPLAINTS(FILENAME TEXT UNIQUE PRIMARY KEY, DEFENDANTS TEXT, PLAINTIFFS TEXT)'
        cursor.execute(create_query)
        conn.commit()
    except sqlite3.Error as e: 
        print(e) 
        abort(500, 'Database error')
    finally:
        conn.close()

if __name__ == '__main__':
    initialize_db()
    app.run()