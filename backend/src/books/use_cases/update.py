import logging

from books import models as bm


logger = logging.getLogger(__name__)


def update_book(book: bm.Book, validated_data: dict) -> bm.Book:
    for key, value in validated_data.items():
        setattr(book, key, value)

    book.save()

    logger.info("book-updated", extra={"user_id": book.user.uuid, "book_id": book.uuid})

    return book
