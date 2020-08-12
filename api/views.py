from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer, TagSerializer
from .serializers import PaymentSerializer, TransactionSerializer
from .serializers import TransactionTypeSerializer, PaymentInitialSerializer
from .models import Category, Tag, Transaction
from .models import Payment, TransactionType, PaymentInitial


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


class PaymentInitialViewSet(BaseViewSet):
    serializer_class = PaymentInitialSerializer
    queryset = PaymentInitial.objects.all()

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

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def get_queryset(self):

        queryset = super().get_queryset()
        query_params = self.request.query_params

        if 'from_date' in query_params.keys():
            from_date = (self.request.query_params['from_date'])
            queryset = queryset.filter(transaction_date__gte=from_date)

        if 'to_date' in query_params.keys():
            to_date = (self.request.query_params['to_date'])
            queryset = queryset.filter(transaction_date__lte=to_date)

        return queryset
