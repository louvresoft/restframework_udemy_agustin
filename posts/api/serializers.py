from rest_framework import serializers

from categories.api.serializers import CategorySerializer
from posts.models import Post
from user.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']

