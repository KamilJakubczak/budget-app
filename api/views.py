from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, TagSerializer

from .serializers import PaymentSerializer, TransactionSerializer
from .serializers import TransactionTypeSerializer, PaymentSumSerializer, CategorySumSerializer, TagSumSerializer, TransactionReadSerializer
from .models import Category, Tag, Transaction
from .models import Payment, TransactionType

from django.db.models import Sum, F, DecimalField
from decimal import Decimal
# class BaseViewSet(viewsets.GenericViewSet,
#                   mixins.ListModelMixin,
#                   mixins.CreateModelMixin):


class BaseViewSet(viewsets.ModelViewSet):
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


class TransactionTypeViewSet(BaseViewSet):
    """
    A simple viewset for creating and editing transaction types

    """

    serializer_class = TransactionTypeSerializer
    queryset = TransactionType.objects.all()


class TransactionViewSet(
    BaseViewSet,
):

    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TransactionReadSerializer
        return TransactionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        query_data = QueryData(queryset, query_params)
        filtered_data = query_data.queryset

        return filtered_data


class PaymentSumView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, requset):

        queryset = Transaction.objects.all()
        query_data = QueryData(
            queryset,
            self.request.query_params)

        query_data.filter_user(self.request.user)
        filtered_data = query_data.queryset

        accounts = Payment.objects.all().filter(user=self.request.user)
        res = []
        for account in accounts:
            response = {}
            payment_target_sum = filtered_data \
                .filter(payment_target=account) \
                .aggregate(Sum('amount'))['amount__sum']

            payment_source_sum = filtered_data \
                .filter(payment_source=account) \
                .aggregate(Sum('amount'))['amount__sum']

            if payment_source_sum is None:
                payment_source_sum = 0

            if payment_target_sum is None:
                payment_target_sum = 0

            response['name'] = account.payment
            response['sum'] = float(payment_target_sum) - \
                float(payment_source_sum)
            res.append(response)
        serializer = PaymentSumSerializer(res, many=True)
        return Response(serializer.data)


class CategorySumView(APIView):
    def get(self, requset):

        queryset = Transaction.objects.values(
            'category__name').annotate(sum=Sum('amount'))

        query_data = QueryData(
            queryset,
            self.request.query_params)

        filtered_data = query_data.queryset
        serializer = CategorySumSerializer(filtered_data, many=True)
        return Response(serializer.data)


class TagSumView(APIView):
    def get(self, requset):

        queryset = Transaction.objects.values(
            'tag__name').annotate(sum=Sum('amount'))

        query_data = QueryData(
            queryset,
            self.request.query_params)

        filtered_data = query_data.queryset
        serializer = TagSumSerializer(filtered_data, many=True)
        return Response(serializer.data)


"""
HELPERS
"""

""" Class for filtering the queryset to provided date range"""


class QueryData:

    def __init__(self, queryset, query_params):
        self.queryset = queryset
        self.query_params = query_params

        self.filter_from()
        self.filter_to()

    def has_key(self, key):
        if key in self.query_params.keys():
            return True
        return False

    def filter_from(self):

        key = 'from_date'
        if self.has_key(key):
            date = self.query_params[key]
            queryset = self.queryset.filter(transaction_date__gte=date)
            self.queryset = queryset

    def filter_to(self):

        key = 'to_date'
        if self.has_key(key):
            date = self.query_params[key]
            queryset = self.queryset.filter(transaction_date__lte=date)
            self.queryset = queryset

    def filter_user(self, user):
        self.queryset = self.queryset.filter(user=user.id)
