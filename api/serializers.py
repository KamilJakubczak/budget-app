from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serizliazer for category object"""

    class Meta:
        model = Category
        fields = ('id', 'name', 'user', 'enabled')
        read_only_fields = ('id',)
