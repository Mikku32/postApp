from django.urls import path
from api.views import PostDetailApiView, PostListApiView


urlpatterns = [
    
    path('posts/', PostListApiView.as_view()), 
    path('posts/<int:pk>/', PostDetailApiView.as_view()),
]