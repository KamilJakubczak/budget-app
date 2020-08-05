from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer, TagSerializer
from .models import Category, Tag


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """
    A simple viewset for creating and editing categories
    """
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    # Required for assigning user when adding new
    # category object

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #  def get_queryset(self):
    #      queryset = Category.objects.all()


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """
    A simple viewset for creating and editing tags
    as

    """

    serializer_class = TagSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #  def get_queryset(self):
    #      queryset = Tag.objects.all()
