#Creating a Book Serializer to convert the Book model instances into JSON format.

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields  = '__all__'

    