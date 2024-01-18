import pytest

from rest_framework import status
from rest_framework.reverse import reverse


pytestmark = pytest.mark.django_db()


def test_successful_login_returns_token(user, api_client):
    temp_pw = "temp-pw-123"
    user.set_password(temp_pw)
    user.save()

    url = reverse("auth:login")
    payload = {"username": user.email, "password": temp_pw}

    response = api_client.post(url, payload)

    assert response.status_code == status.HTTP_200_OK
    assert "token" in response.data
