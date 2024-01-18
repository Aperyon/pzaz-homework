from logging import warn
import pytest

from rest_framework import status
from rest_framework.reverse import reverse


pytestmark = pytest.mark.django_db()


def test_can_see_own_book_only(book, book2, user_api_client):
    url = reverse("api:book-list")

    response = user_api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["uuid"] == str(book.uuid)


def test_unauthenticad_user_not_allowed(book, api_client):
    url = reverse("api:book-list")

    response = api_client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
