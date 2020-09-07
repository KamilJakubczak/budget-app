from rest_framework import serializers

from .models import Category, Tag, Transaction
from .models import Payment, TransactionType


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    """
    Alternative for related field that gives posibility
    to set desireable object representation
    after parent object creation
    """

    def __init__(self, **kwargs):

        self.object_attr = kwargs.pop('field_name', None)
        self.serializer = kwargs.pop('serializer', None)

        if self.serializer is not None and not issubclass(
            self.serializer,
            serializers.Serializer
        ):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):

        if self.serializer and self.object_attr is None:
            return self.serializer(
                instance,
                context=self.context
            ).data

        if self.object_attr is not None:
            return self.serializer(
                instance,
                context=self.context
            ).data[self.object_attr]

        return super().to_representation(instance)


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
    category = RelatedFieldAlternative(
        queryset=Category.objects.all(),
        serializer=CategorySerializer,
        field_name='name'
    )

    transaction_type = RelatedFieldAlternative(
        queryset=TransactionType.objects.all(),
        serializer=TransactionTypeSerializer,
        field_name='transaction_type'
    )

    tag = RelatedFieldAlternative(
        queryset=Tag.objects.all(),
        serializer=TagSerializer,
        field_name='name',
        allow_null=True
    )

    payment_target = RelatedFieldAlternative(
        queryset=Payment.objects.all(),
        serializer=PaymentSerializer,
        field_name='payment',
        allow_null=True
    )

    payment_source = RelatedFieldAlternative(
        queryset=Payment.objects.all(),
        serializer=PaymentSerializer,
        field_name='payment',
        allow_null=True
    )

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {
                'required': False
            },
            'tag': {
                'required': False
            }

        }


class TransactionReadSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(
        many=False,
        read_only=True)

    tag = serializers.StringRelatedField(
        many=False,
        read_only=True)

    transaction_type = serializers.StringRelatedField(
        many=False,
        read_only=True)

    payment_target = serializers.StringRelatedField(
        many=False,
        read_only=True)

    payment_source = serializers.StringRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = Transaction
        read_only_fields = ('id',)
        exclude = ('user',)


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
