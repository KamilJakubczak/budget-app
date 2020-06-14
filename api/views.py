from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer
from .models import Category
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for creating and editing categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
