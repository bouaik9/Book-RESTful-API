from django.shortcuts import render
from rest_framework import generics

from Book_api.serializer import BookSerializer, AuthorSerializer, GenreSerializer
from .models import Book, Author, Genre


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
