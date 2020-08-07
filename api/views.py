from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer, TagSerializer
from .serializers import PaymentSerializer, TransactionSerializer
from .serializers import TransactionTypeSerializer
from .models import Category, Tag, Transaction
from .models import Payment, TransactionType


class BaseViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """
    A simple base viewset for creating and editing
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(BaseViewSet):
    """
    A simple viewset for creating and editing categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagViewSet(BaseViewSet):
    """
    A simple viewset for creating and editing tags

    """

    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class PaymentViewSet(BaseViewSet):
    """
    A simple viewset for creating and editing Payments

    """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_queryset(self):
        """Return object for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset

        if assigned_only:
            queryset = queryset.filter(payment__isnull=False)
        return queryset.filter(
            user=self.request.user)


class TransactionTypeViewSet(BaseViewSet):
    """
    A simple viewset for creating and editing transaction types

    """

    serializer_class = TransactionTypeSerializer
    queryset = TransactionType.objects.all()

class TransactionViewSet(BaseViewSet):
    """
    A simple viewset for creating and editing Transaction

    """

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
