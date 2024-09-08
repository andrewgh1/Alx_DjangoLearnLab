from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='testuser1', password='testpass123')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass123')
        
        # Create test authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')
        
        # Create test books
        self.book1 = Book.objects.create(title='Test Book 1', publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title='Test Book 2', publication_year=2021, author=self.author2)

    def test_list_books(self):
        """Test retrieving a list of books"""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('book-create')
        data = {'title': 'New Test Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        """Test retrieving a specific book"""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')

    def test_update_book(self):
        """Test updating a book"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Updated Test Book 1', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book1.id).title, 'Updated Test Book 1')

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.force_authenticate(user=self.user1)
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by publication year"""
        url = reverse('book-list') + '?publication_year=2020'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_search_books(self):
        """Test searching books"""
        url = reverse('book-list') + '?search=Test Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_order_books(self):
        """Test ordering books"""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')

    def test_unauthenticated_create(self):
        """Test creating a book without authentication"""
        url = reverse('book-create')
        data = {'title': 'Unauthenticated Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_update(self):
        """Test updating a book without proper permissions"""
        self.client.force_authenticate(user=self.user2)  # Authenticate as a different user
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Unauthorized Update', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)