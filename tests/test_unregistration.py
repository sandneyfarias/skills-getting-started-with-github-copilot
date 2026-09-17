from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "student@example.edu"

    app_module = __import__("src.app", fromlist=["activities"])
    activities = app_module.activities
    if email in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].remove(email)

    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200

    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]

    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert response.status_code == 404
