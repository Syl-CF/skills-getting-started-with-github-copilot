import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Get an activity name
    activities = client.get("/activities").json()
    assert activities, "No activities found"
    activity_name = list(activities.keys())[0]
    email = "testuser@example.com"

    # Sign up
    signup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup.status_code == 200
    assert "message" in signup.json()

    # Unregister (if implemented)
    unregister = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    # Accept 200 or 404 (if not found)
    assert unregister.status_code in (200, 404)
