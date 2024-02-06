from django.shortcuts import render
from rest_framework import generics

from api.models import Post
from api.serializers import PostSerializer

# Create your views here.


class PostListApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer