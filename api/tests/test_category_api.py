from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.models import Category

CATEGORY_URL = reverse('api:category-list')


class PublicTestCase(TestCase):
    """
    Test for publicy avaialable category API
    """

    def setUp(self):

        self.client = APIClient()

    def test_login_required(self):
        """
        Tests if login is required for retriving categories
        """

        res = self.client.get(CATEGORY_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTestCase(TestCase):
    """
    Test for private category API
    """

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            'testuser',
            'supertest'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_creating_category(self):

        payload = {
            'name': 'test',
            'user_id': self.user.id}

        self.client.post(CATEGORY_URL, payload)
        response = Category.objects.get(user_id=self.user.id).__str__()

        self.assertEqual(
                response,
                self.user.username + ' - ' + payload['name'])
