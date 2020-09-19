from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.models import Category, TransactionType

category_URL = reverse('api:category-list')


def detail_url(category_id):
    return reverse('api:category-detail', args=[category_id])


def sample_transaction_type(user, **params):
    """Create and return a sampe recipe"""
    defaults = {
        'transaction_type': 'test_type',
    }
    defaults.update(params)

    return TransactionType.objects.create(user=user, **defaults)


def sample_category(user, **params):
    """Create and return a sampe recipe"""
    defaults = {
        'name': 'test_category',
        'transaction_type_id': sample_transaction_type(user).id,
    }
    defaults.update(params)
    return Category.objects.create(user=user, **defaults)


class PublicTestCase(TestCase):
    """
    Test for publicy avaialable category API
    """

    def setUp(self):

        self.client = APIClient()

    def test_login_required(self):
        """
        Tests if login is required for retriving categorys
        """
        res = self.client.get(category_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTestCase(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            'testuser',
            'supertest'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_login_required_ok(self):
        """
        Test getting categories for logged in user
        """

        sample_category(self.user)
        res = self.client.get(category_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_getting_all_categories(self):
        """
        Test getting all categories
        """

        sample_category(self.user)
        sample_category(self.user, name='test_category2')
        res = self.client.get(category_URL)

        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['name'], 'test_category')
        self.assertEqual(res.data[1]['name'], 'test_category2')

    def test_getting_single_category(self):
        """
        Testing getting single category
        """

        sample_category(self.user)
        category2 = sample_category(
            self.user,
            name='test2')

        url = detail_url(category2.id)
        res = self.client.get(url)

        self.assertFalse(isinstance(res.data, list))
        self.assertEqual(res.data['name'], 'test2')

    def test_getting_categories_assined_to_user(self):
        """
        Test filtering categories for logged user
        """

        self.user2 = get_user_model().objects.create_user(
            'testuser2',
            'supertest'
        )

        sample_category(self.user, name='food')
        sample_category(self.user2, name='transport')

        res = self.client.get(category_URL)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], 'food')

    def test_retrieve_recursicved_category_name(self):

        category1 = sample_category(
            user=self.user,
            name='category1')

        category2 = sample_category(
            user=self.user,
            name='category2',
            parent_category=category1
        )

        category3 = sample_category(
            user=self.user,
            name='category3',
            parent_category=category2
        )

        expected1 = 'category1'
        self.assertEqual(category1.__str__(), expected1)

        expected2 = 'category1 - category2'
        self.assertEqual(category2.__str__(), expected2)

        expected3 = 'category1 - category2 - category3'
        self.assertEqual(category3.__str__(), expected3)
