import pytest

from rest_framework import status
from rest_framework.reverse import reverse

from books import models as m


pytestmark = pytest.mark.django_db()


def test_user_deletes_own_book(book, user_api_client):
    url = reverse("api:book-detail", kwargs={"uuid": book.uuid})

    response = user_api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    assert not m.Book.objects.exists()


def test_user_can_not_delete_others_books(book, user_api_client, user2):
    book.user = user2
    book.save()

    url = reverse("api:book-detail", kwargs={"uuid": book.uuid})

    response = user_api_client.delete(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_unauthenticated_user_is_not_allowed(book, api_client):
    url = reverse("api:book-detail", kwargs={"uuid": book.uuid})

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
