from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for creating and editing categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer