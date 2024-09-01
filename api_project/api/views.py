from django.shortcuts import render
from rest_framework import generics 
from .models import Book 
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet to view and edit book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer