from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth

import app

client = TestClient(app.app)

auth = HTTPBasicAuth('admin', 'password123') # Create an HTTPBasicAuth login
bad_auth = HTTPBasicAuth('admin', 'badpassword')

def test_read_main_alert_authorized():
    response = client.get("/alerts", auth=auth)
    assert response.status_code == 200 # Check for authorized status code
