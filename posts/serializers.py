from rest_framework import serializers
from .models import NewsPost, Comment
from accounts.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created_at']
# Compare this snippet from posts/permissions.py:
# from rest_framework import permissions    
#
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}