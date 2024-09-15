from django.urls import path
from .views import LoginView, register, LogoutView, profile, edit_profile, CreateView, UpdateView, DetailView, DeleteView, ListView
from . import views
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile' ),
    path('post/new/', views.CreateView.as_view(), name='post_create'),
    path('', views.ListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('post/<int:pk>/edit/', views.UpdateView.as_view(), name='post_update'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/create/',views.CommentCreateView.as_view(), name="comment_create"),
    path('tag/<str:tag_name>/', views.tag_posts, name='tag_posts'),

]

 
    
    
    

    