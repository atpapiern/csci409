from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth

import app

client = TestClient(app.app)

auth = HTTPBasicAuth('admin', 'password123') # Create an HTTPBasicAuth login
bad_auth = HTTPBasicAuth('admin', 'badpassword')

# Test unauthorized vehicle
def test_read_main_vehicle_unauthorized_nologin():
    response = client.get("/vehicles")
    assert response.status_code == 401 # Check for unauthorized status code

# Test Unauthorized vehicle
def test_read_main_vehicle_unauthorized_bad_credentials():
    response = client.get("/vehicles", auth=bad_auth)
    assert response.status_code == 401 # Check for unauthorized status code

def test_read_main_vehicle_authorized():
    response = client.get("/vehicles", auth=auth)
    assert response.status_code == 200 # Check for authorized status code

def test_read_vehicle_content():
    response = client.get("/vehicles/y0832", auth=auth)
    vehicle = response.json().get("vehicle") # Fetch vehicle details from json response
    assert response.status_code == 200 # Check status code is 200 ok
    # Verify line details
    #assert vehicle.get("id") == 'y0832'

def test_read_vehicle_not_found():
    vehicle_id = "Chauncey"
    response = client.get(f"/vehicles/{vehicle_id}", auth=auth)
    assert response.status_code == 404
    print(response.json())
    assert response.json().get("message") == f"Vehicle {vehicle_id} not found"

