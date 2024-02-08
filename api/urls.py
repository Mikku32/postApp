from django.urls import path
from api.views import CommentDetailApiView, CommentListApiView, LikeListApiView, PostDetailApiView, PostListApiView, UserDetailApiView, UserListApiView


urlpatterns = [
    
    path('posts/', PostListApiView.as_view()), 
    path('posts/<int:pk>/', PostDetailApiView.as_view()),

    path('users/', UserListApiView.as_view()),
    path('users/<int:pk>/', UserDetailApiView.as_view()),

    path('comments/', CommentListApiView.as_view()),
    path('comments/<int:pk>/', CommentDetailApiView.as_view()),


    path('likes/', LikeListApiView.as_view()),

]