import logging

from books import models as bm


logger = logging.getLogger(__name__)


def delete_book(book: bm.Book) -> None:
    book.delete()

    logger.info("book-updated", extra={"user_id": book.user.uuid, "book_id": book.uuid})
