import uuid

from django.db import models


class Book(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=False, editable=False, unique=True
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    cover_image = models.ImageField(upload_to="book_covers", blank=True, default="")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
