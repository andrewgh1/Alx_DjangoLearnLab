from api.models import Author, Book
from rest_framework import serializers
from api.serializers import AuthorSerializer, BookSerializer
from django.utils import timezone

# Creating test data
author = Author.objects.create(name="Andrew A. Laryea")
book1 = Book.objects.create(title="Advanced Api Project with Django", publication_year=2024, author=author)
book2 = Book.objects.create(title="Use of Custom Serializers", publication_year=2021, author=author)

# Testing AuthorSerializer
author_serializer = AuthorSerializer(author)
print("Author Serializer Output:")
print(author_serializer.data)

# Testing BookSerializer
book_serializer = BookSerializer(book1)
print("\nBook Serializer Output:")
print(book_serializer.data)

# Testing validation
try:
    invalid_book = BookSerializer(data={'title': 'Future Book', 'publication_year': timezone.now().year + 1, 'author': author.id})
    invalid_book.is_valid(raise_exception=True)
except serializers.ValidationError as e:
    print("\nValidation Error (as expected):")
    print(e)