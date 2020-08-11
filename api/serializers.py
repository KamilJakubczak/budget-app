from rest_framework import serializers

from .models import Category, Tag, Transaction
from .models import Payment, TransactionType


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id',)

class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment object"""

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('id',)

class TransactionTypeSerializer(serializers.ModelSerializer):
    """Serializer for transaction type object"""

    class Meta:
        model = TransactionType
        fields = '__all__'
        read_only_fields = ('id',)

class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for Transaction object"""

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('id',)
