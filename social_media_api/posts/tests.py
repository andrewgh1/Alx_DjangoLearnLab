# posts/tests.py

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from django.contrib.auth import get_user_model
from .models import Post, Like
from notifications.models import Notification

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = reverse('post-list')
        data = {'title': 'Test Post', 'content': 'This is a test post.'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_update_post(self):
        post = Post.objects.create(author=self.user, title='Original Post', content='Original content')
        url = reverse('post-detail', kwargs={'pk': post.id})
        data = {'title': 'Updated Post', 'content': 'Updated content'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().title, 'Updated Post')

    def test_delete_post(self):
        post = Post.objects.create(author=self.user, title='Test Post', content='Test content')
        url = reverse('post-detail', kwargs={'pk': post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class LikeTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.post = Post.objects.create(author=self.user2, title='Test Post', content='This is a test post.')
        self.client.force_authenticate(user=self.user1)

    def test_like_post(self):
        url = reverse('post-like', kwargs={'pk': self.post.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Like.objects.filter(user=self.user1, post=self.post).exists())
        self.assertTrue(Notification.objects.filter(recipient=self.user2, actor=self.user1, verb='liked').exists())

    def test_unlike_post(self):
        Like.objects.create(user=self.user1, post=self.post)
        url = reverse('post-unlike', kwargs={'pk': self.post.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Like.objects.filter(user=self.user1, post=self.post).exists())

class NotificationTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.post = Post.objects.create(author=self.user2, title='Test Post', content='This is a test post.')
        self.client.force_authenticate(user=self.user2)

    def test_get_notifications(self):
        Notification.objects.create(recipient=self.user2, actor=self.user1, verb='liked', target=self.post)
        url = reverse('notification-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['verb'], 'liked')