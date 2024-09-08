from .models import Author, Book
from rest_framework import serializers
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    This serializer handles the serialization and deserialization of Book instances,
    including custom validation for the publication_year field.
    """
    class Meta:
        model = Book
        fields = "__all__"
    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication_year is not in the future.
        """
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    
    This serializer includes a nested representation of the author's books,
    demonstrating how to handle nested relationships in DRF.
    """
    books = BookSerializer(many=True, read_only=True)

    

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
    
    def to_representation(self, instance):
        """
        Custom representation to include the count of books for each author.
        """
        representation = super().to_representation(instance)
        representation['books_count'] = instance.books.count()
        return representation

    