from django.contrib import admin

from . import models as m


class BookAdmin(admin.ModelAdmin):
    list_display = ["uuid", "user", "title", "author", "has_cover_image"]

    def has_cover_image(self, obj):
        return bool(obj.cover_image)


admin.site.register(m.Book, BookAdmin)
