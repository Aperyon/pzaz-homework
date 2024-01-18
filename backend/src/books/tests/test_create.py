import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from books import models as m


pytestmark = pytest.mark.django_db()


def test_user_creates_book(user, user_api_client):
    url = reverse("api:book-list")
    payload = {"title": "Test Book #1", "description": "Test Book #1 - Description"}

    response = user_api_client.post(url, payload)

    assert response.status_code == status.HTTP_201_CREATED, response.data
    assert response.data["title"] == payload["title"]
    assert response.data["description"] == payload["description"]

    book = m.Book.objects.first()
    if not book:
        assert False

    assert book.user == user


def test_unauthenticated_user_is_not_allowed(api_client):
    url = reverse("api:book-list")
    payload = {"title": "Test Book #1", "description": "Test Book #1 - Description"}

    response = api_client.post(url, payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
