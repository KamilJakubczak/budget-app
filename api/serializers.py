from rest_framework import serializers

from .models import Category, Tag, Transaction
from .models import Payment, TransactionType, PaymentInitial


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""

    class Meta:
        model = Category
        fields = '__all__'
        # read_only_fields = ('id',)


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


class PaymentInitialSerializer(serializers.ModelSerializer):
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


class PaymentSumSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    sum = serializers.DecimalField(
        max_digits=10,
        decimal_places=2)


class CategorySumSerializer(serializers.Serializer):
    category__name = serializers.CharField(max_length=200)
    sum = serializers.DecimalField(
        max_digits=10,
        decimal_places=2)


class TagSumSerializer(serializers.Serializer):
    tag__name = serializers.CharField(max_length=200)
    sum = serializers.DecimalField(
        max_digits=10,
        decimal_places=2)
