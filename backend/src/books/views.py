from rest_framework import viewsets


from . import models as m
from . import serializers as s
from .use_cases import delete as d


class BookViewSet(viewsets.ModelViewSet):
    queryset = m.Book.objects.all()
    serializer_class = s.BookSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_destroy(self, instance):
        d.delete_book(instance)
