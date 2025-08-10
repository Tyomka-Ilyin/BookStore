from django.contrib import admin
from . models import Book, Genre, BookGenre, NDS

admin.site.register(Genre)
admin.site.register(BookGenre)
admin.site.register(NDS)

class GenreInlineAdmin(admin.StackedInline):
    model = BookGenre

class NDSinBookAdmin(admin.StackedInline):
    model = NDS

class BookAdmin(admin.ModelAdmin):
    model=Book

    inlines = [GenreInlineAdmin, NDSinBookAdmin]

admin.site.register(Book, BookAdmin)