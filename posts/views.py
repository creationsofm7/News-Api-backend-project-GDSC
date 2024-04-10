from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import NewsPost, Comment
from .serializers import PostSerializer, CommentSerializer


class PostList(generics.ListCreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

class PostCreate(generics.CreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated) 