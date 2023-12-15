from django.contrib import admin

from Book_api.models import Book, Genre, Author

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
