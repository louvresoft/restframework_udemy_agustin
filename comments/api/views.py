from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.models import Comment

from comments.api.serializers import CommentSerializer


class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['post']


# http://localhost:8000/api/comments/?post=2
# filtra por post
