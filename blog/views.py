import json
from django.shortcuts import render
from rest_framework import generics, permissions
from django.http import JsonResponse
from django.contrib.auth.models import User
import django.middleware

# Create your views here.

from .models import Post
from .serializers import PostSerializer

def get_csrf_token(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'token': token})

def register_user(request):
    if request.method == 'POST':
        # Extract user registration information from the POST request
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        email = body.get('email')
        # Create a new user in the Django database
        user = User.objects.create_user(username=username, email=email, password=password)

        # Return a JSON response with the new user's ID
        return JsonResponse({'user_id': user.id})

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer