# core/urls.py
from django.urls import path
from .views import (

    SignupAPIView, CustomAuthToken,
    PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView,
    LikePostAPIView, CommentListCreateAPIView,
)

urlpatterns = [
  
    
    path('api/signup/', SignupAPIView.as_view(), name='api_signup'),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),

    path('api/posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),

    path('api/posts/<int:post_id>/like/', LikePostAPIView.as_view(), name='post_like'),

    path('api/comments/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
]
