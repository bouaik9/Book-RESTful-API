from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    # Basic Information
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    publication_date = models.DateField()

    # Additional Information
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True, null=True)
    
    # Image Field
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, default=None)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)  # A brief biography of the author

    # Additional Information
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    




class Genre(models.Model):
    # Genre Information
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
