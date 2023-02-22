from django.contrib import admin
from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "public_site")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_editable = ("public_site",)


admin.site.register(Books, BooksAdmin)
