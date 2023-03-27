from django.urls import path
from .views import PostList, PostDetail, register_user, get_csrf_token

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('register_user/', register_user, name='register_user'),
    path('get_csrf_token/', get_csrf_token, name='get_csrf_token')
]