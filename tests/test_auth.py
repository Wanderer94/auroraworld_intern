from tests.conftest import client


def test_register_user():
    """회원가입 API 테스트"""
    response = client.post(
        "/users/", json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_login():
    """JWT 로그인 API 테스트"""
    client.post(
        "/users/", json={"username": "testuser", "password": "testpass"}
    )  # 회원가입
    response = client.post(
        "/auth/login", data={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
