from rest_framework import serializers

from . import models as m
from .use_cases import create as c
from .use_cases import update as u


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = m.Book
        fields = ["url", "uuid", "title", "description", "cover_image"]
        extra_kwargs = {
            "url": {"view_name": "api:book-detail", "lookup_field": "uuid"},
        }

    def create(self, validated_data):
        return c.create_book(self.context["request"].user, validated_data)

    def update(self, instance, validated_data):
        return u.update_book(instance, validated_data)
