from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import complaint_parser
import sqlite3

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/', methods = ['GET', 'POST'])
def mainpage():
    return render_template('mainpage.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return process_xml(f.read())

def process_xml(xml_text):
    return xml_text

if __name__ == '__main__':
    app.run()