from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
import os
import complaint_parser
import sqlite3
import json

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

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
    return True

def process_xml(file):
    complaint_dict = {}
    complaint_dict['filename'] = file.filename
    filetext = file.read().decode('utf-8')
    complaint_dict['defendants'] = complaint_parser.get_defendants_from_xml(filetext)
    complaint_dict['plaintiffs'] = complaint_parser.get_plaintiffs_from_xml(filetext)
    complaint_json = json.dumps(complaint_dict)
    return complaint_json

if __name__ == '__main__':
    app.run()