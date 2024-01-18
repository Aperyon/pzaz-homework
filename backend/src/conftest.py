import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from books import models as bm
from users import models as um


@pytest.fixture
def user():
    user = um.User.objects.create(email="testuser1@email.com")
    user.set_password("some-fake-and-complex-password")
    user.save()
    return user


@pytest.fixture
def user2():
    user = um.User.objects.create(email="testuser2@email.com")
    user.set_password("some-fake-and-complex-password")
    user.save()
    return user


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def user_api_client(user):
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    return client


@pytest.fixture
def book(user):
    return bm.Book.objects.create(title="Test Book #1", user=user)


@pytest.fixture
def book2(user2):
    return bm.Book.objects.create(title="Test Book #2", user=user2)
