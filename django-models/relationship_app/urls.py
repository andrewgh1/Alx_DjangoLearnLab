from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, profile_view
from .views import list_books, LibraryDetailView,
urlpatterns = [
    path('', views.home, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'), 
]