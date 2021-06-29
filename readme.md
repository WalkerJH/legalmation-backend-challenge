# LegalMation Backend Coding Challenge: Complaint API

**By Walker Herring**

Requirements to run the app: Python3, Flask 2.0.1, requests, sqlite3, xml.ElementTree \
Required to run included tests: pytest \
To run the app, first clone the repository. Then, using your terminal, navigate to the project directory and run the following command:
```
$ python3 flask_app.py
```

## Web App

After running the app locally, open it by navigating to http://127.0.0.1:5000/ in your web browser. \
Click **browse** to select an xml file you have generated from a legal complaint. Only xml files generated with ABBYY FineReader will be accepted.
Then, click **Upload & Process**.

You will be redirected to JSON containing your plaintiffs and defendants. From there, you can save the page to your machine.

## API Documentation

The API follows the [JSON:API Specification](https://jsonapi.org/format/). \
After an xml document is processed, the API responds with JSON containing:
- **filename:** String. Name of the file you uploaded.
- **defendants:** String. Defendant or defendants parsed from the xml complaint.
- **plaintiffs:** String. Plaintiff or plaintiffs parsed from the xml complaint.

### Example

```
{
  "data": {
    "attributes": {
      "defendants": "Business Inc",
      "filename": "my_complaint.xml",
      "plaintiffs": "Jane Doe"
    },
    "id": "1",
    "type": "complaint"
  }
}
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
