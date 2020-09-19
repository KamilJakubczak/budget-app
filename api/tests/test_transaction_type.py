from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.models import TransactionType

transaction_types_URL = reverse('api:types-list')


def detail_url(transaction_type_id):
    return reverse('api:types-detail', args=[transaction_type_id])


def sample_transaction_type(user, **params):
    """Create and return a sampe recipe"""
    defaults = {
        'transaction_type': 'test_type',
    }
    defaults.update(params)

    return TransactionType.objects.create(user=user, **defaults)


class PublicTestCase(TestCase):
    """
    Test for publicy avaialable category API
    """

    def setUp(self):

        self.client = APIClient()

    def test_login_required_error(self):
        """
        Tests if login is required for retriving categorys
        """
        res = self.client.get(transaction_types_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class ModelTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            'testuser',
            'supertest'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_login_required_ok(self):
        """
        Test getting transaction tags for logged in users
        """

        TransactionType.objects.create(
            user=self.user,
            transaction_type='test'
        )
        res = self.client.get(transaction_types_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_getting_all_transaction_types(self):
        """
        Test getting all transaction types
        """

        TransactionType.objects.create(
            user=self.user,
            transaction_type='test'
        )
        TransactionType.objects.create(
            user=self.user,
            transaction_type='test2'
        )
        res = self.client.get(transaction_types_URL)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['transaction_type'], 'test')
        self.assertEqual(res.data[1]['transaction_type'], 'test2')

    def test_getting_single_transaction_type(self):
        """
        Testing getting single transaction
        """

        sample_transaction_type(self.user)
        type2 = sample_transaction_type(
            self.user,
            transaction_type='cash')

        url = detail_url(type2.id)
        res = self.client.get(url)

        self.assertFalse(isinstance(res.data, list))
        self.assertEqual(res.data['transaction_type'], 'cash')

    def test_getting_transaction_types_assined_to_user(self):
        """
        Test filtering the transaction types, for logged user
        """

        self.user2 = get_user_model().objects.create_user(
            'testuser2',
            'supertest'
        )

        sample_transaction_type(self.user, transaction_type='cash')
        sample_transaction_type(self.user2, transaction_type='account')

        res = self.client.get(transaction_types_URL)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['transaction_type'], 'cash')
