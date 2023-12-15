from rest_framework import serializers
from .models import Book, Author, Genre



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorNameSerializer()
    genre = GenreNameSerializer()
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'isbn', 'description']


