def test_get_activities(client, isolated_activities):
    """Test GET /activities returns all activities"""
    # Arrange
    expected_activities = isolated_activities

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_activities


def test_signup_for_activity_success(client, isolated_activities):
    """Test successful signup adds participant to activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in isolated_activities[activity_name]["participants"]


def test_unregister_from_activity_success(client, isolated_activities):
    """Test successful unregister removes participant from activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    assert email in isolated_activities[activity_name]["participants"]

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in isolated_activities[activity_name]["participants"]
