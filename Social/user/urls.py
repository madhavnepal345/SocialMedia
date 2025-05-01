# core/urls.py
from django.urls import path
from .views import (
    signup_view, login_view, logout_view, home_view,
    like_post, add_comment,
    SignupAPIView, CustomAuthToken,
    PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView,
    LikePostAPIView, CommentListCreateAPIView,
)

urlpatterns = [
    # Frontend Views
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),

    # API endpoints
    path('api/signup/', SignupAPIView.as_view(), name='api_signup'),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),

    path('api/posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),

    path('api/posts/<int:post_id>/like/', LikePostAPIView.as_view(), name='post_like'),

    path('api/comments/', CommentListCreateAPIView.as_view(), name='comment_list_create'),
]
