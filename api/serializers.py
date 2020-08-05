from rest_framework import serializers

from .models import Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    """Serizliazer for category object"""

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)


class TagSerializer(serializers.ModelSerializer):
    """Serizliazer for tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name', 'parent_tag')
        read_only_fields = ('id',)
