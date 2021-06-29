# LegalMation Backend Coding Challenge
By Walker Herring

Requirements to run the app: Python3, Flask 2.0.1, requests, sqlite3, xml.ElementTree \\
Required to run included tests: pytest \\
To run the app, first clone the repository. In your terminal, navigate to the project directory and run the following command:
```
$ python3 flask_app.py
```

## Web App
To use the web app, navigate to http://127.0.0.1:5000/.
Click "browse" to select an xml file you have generated from a legal complaint.
Then, click the "Upload & Process" button.

You will be redirected to JSON containing your plaintiffs and defendants. From there, you can save the page to your machine.

## API Documentation
The API follows the [JSON:API Specification](https://jsonapi.org/format/). \\
After an xml document is processed, the API responds with JSON in this form:
```
json here
```

### curl Usage

To upload your file, run this command in your terminal:
```
$ curl -F 'file=@<my_file_path>' http://127.0.0.1:5000/ 
```
The api will respond with JSON containing your plaintiffs and defendants.

### Python Usage
```
files = {'file': open('<my_file_path>', 'rb')}
r = requests.post(local_host_url, files = files)
complaint_info = r.json
```
This code uploads the file at my_file_path and stores the JSON received from the API in the variable complaint_info. 

After your XML file is processed, you will 