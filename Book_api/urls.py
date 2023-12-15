from django.urls import path
from .views import BookListView, AuthorListView, GenreListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('genres/', GenreListView.as_view(), name='genre-list'),

    # Add other URL patterns as needed
]