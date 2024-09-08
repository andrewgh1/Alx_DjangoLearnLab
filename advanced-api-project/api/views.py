from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly

class BookListView(generics.ListCreateAPIView):
    """
    API view to retrieve list of books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        """
        Custom update method to handle additional logic if needed.
        """
        # Add any custom logic here before saving
        serializer.save()

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom create method to handle additional logic if needed.
        """
        # Add any custom logic here before saving
        serializer.save(author=self.request.user)


