from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


from api.models import Category

CATEGORY_URL = reverse('api:category-list')


class CategoryTestCase(TestCase):
    """
    Test for publicy available category API
    """

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """
        Tests if login is required for retriving categories
        """

        res = self.client.get(CATEGORY_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
