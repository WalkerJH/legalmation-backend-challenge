from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
import os
import complaint_parser
import sqlite3

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 4
app.config['UPLOAD_EXTENSIONS'] = ['.xml']

@app.route('/', methods = ['GET', 'POST'])
def mainpage():
    r = render_template('mainpage.html')
    if request.method == 'POST':
        print("processing file!")
        file = request.files['file']
        print(file.filename)
        if (validate_file(file)):
            print("file validated!")
            r = process_xml(file.read())
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
    return True

def process_xml(xml_text):
    return xml_text

if __name__ == '__main__':
    app.run()