import logging

from books import models as bm
from users import models as um


logger = logging.getLogger(__name__)


def create_book(user: um.User, validated_data) -> bm.Book:
    book = bm.Book.objects.create(user=user, **validated_data)

    logger.info("book-created", extra={"user_id": user.uuid, "book_id": book.uuid})

    return book
