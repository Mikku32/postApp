
from django.shortcuts import render
from rest_framework import generics

from api.models import Like, Post, User, Comment
from api.serializers import CommentSerializer, LikeSerializer, PostSerializer, UserSerializer

# Create your views here.


class PostListApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    

class UserListApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentListApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    

class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeListApiView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer        