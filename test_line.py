from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth

import app

client = TestClient(app.app)

auth = HTTPBasicAuth('admin', 'password123') # Create an HTTPBasicAuth login
bad_auth = HTTPBasicAuth('admin', 'badpassword')

# Test unauthorized line
def test_read_main_line_unauthorized_nologin():
    response = client.get("/lines")
    assert response.status_code == 401 # Check for unauthorized status code

# Test Unauthorized line
def test_read_main_line_unauthorized_bad_credentials():
    response = client.get("/lines", auth=bad_auth)
    assert response.status_code == 401 # Check for unauthorized status code

def test_read_main_line_authorized():
    response = client.get("/lines", auth=auth)
    assert response.status_code == 200 # Check for authorized status code

def test_read_line_content():
    response = client.get("/lines/line-Red", auth=auth)
    line = response.json().get("line") # Fetch line details from json response
    assert response.status_code == 200 # Check status code is 200 ok
    #Verify line details
    assert line.get("id") == 'line-Red'
    assert line.get("color") == 'DA291C'
    assert line.get("text_color") == 'FFFFFF'
    assert line.get("short_name") == ''
    assert line.get("long_name") == 'Red Line'

def test_read_line_not_found():
    line_id = "Chauncey"
    response = client.get(f"/lines/{line_id}", auth=auth)
    assert response.status_code == 404
    print(response.json())
    assert response.json().get("message") == f"Line {line_id} not found"

