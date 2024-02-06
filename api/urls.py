from django.urls import path
from api.views import PostDetailApiView, PostListApiView


urlpatterns = [
    
    path('post/', PostListApiView.as_view()), 
    path('post/<int:pk>/', PostDetailApiView.as_view()),
]