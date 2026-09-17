from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.edu"
    app_module = __import__("src.app", fromlist=["activities"])
    activities = app_module.activities

    if email in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].remove(email)

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    unregister_response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert email not in activities[activity_name]["participants"]

    # Act
    second_unreg_response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert second_unreg_response.status_code == 404
