from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #queryset = Category.objects.all()
    queryset = Category.objects.all()
    lookup_field = 'slug'
    # busca por propiedad slug en vez que por id
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']
    # con los filter los pasa como parametors en la url ejemplo
    # localhost:8000/api/categories/?published=false
