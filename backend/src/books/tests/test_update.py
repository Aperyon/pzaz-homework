import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from books import models as m


pytestmark = pytest.mark.django_db()


def test_user_updates_own_book(book, user_api_client):
    url = reverse("api:book-detail", kwargs={"uuid": book.uuid})
    payload = {"title": "Other Test Book #1"}

    response = user_api_client.patch(url, payload)

    assert response.status_code == status.HTTP_200_OK

    book.refresh_from_db()
    assert book.title == payload["title"]


def test_user_can_not_update_others_books(book, user_api_client, user2):
    book.user = user2
    book.save()

    url = reverse("api:book-detail", kwargs={"uuid": book.uuid})
    payload = {"title": "Other Test Book #1"}

    response = user_api_client.patch(url, payload)

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_unauthenticated_user_is_not_allowed(book, api_client):
    url = reverse("api:book-detail", kwargs={"uuid": book.uuid})
    payload = {"title": "Other Test Book #1"}

    response = api_client.patch(url, payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
