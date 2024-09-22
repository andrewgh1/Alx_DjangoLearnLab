# social_media_api/accounts/urls.py

from django.urls import path
from .views import ( UserRegistrationView, UserLoginView, UserProfileView, FollowUserView, UnfollowUserView)

urlpatterns = [

    # Registration/Login/Profile URLs
    path('register/', UserRegistrationView.as_view(), name='register'), # User registration
    path('login/', UserLoginView.as_view(), name='login'), # User login
    path('profile/', UserProfileView.as_view(), name='profile'), # User profile management

    # Follow/Unfollow URLs
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'), # Follow
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'), # Unfollow
]