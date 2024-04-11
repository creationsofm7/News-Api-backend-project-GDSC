from django.urls import path

from .views import PostList, PostDetail, CommentList, CommentDetail, SignUpView, PostCreate, CommentCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='news_post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='news_post_detail'),
    path('comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create/', PostCreate.as_view(), name='create_post'),
    path('create_comment/', CommentCreate.as_view(), name='create_comment'),
]