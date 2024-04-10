from django.urls import path

from .views import PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='news_post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='news_post_detail'),
    path('comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
]