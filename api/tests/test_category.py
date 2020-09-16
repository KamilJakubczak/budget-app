from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.models import Category

category_URL = reverse('api:category-list')


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


# class ModelTests(TestCase):

#     def setUp(self):

#         self.user = get_user_model().objects.create_user(
#             'testuser',
#             'supertest'
#         )
#         self.client = APIClient()

#     def test_retrieve_recursd_category_name(self):
#         category1 = Category.objects.create(name='category1',
#                                   user=self.user)

#         category2 = Category.objects.create(name='category2',
#                                   user=self.user,
#                                   parent_category=category1)

#         category3 = Category.objects.create(name='category3',
#                                   user=self.user,
#                                   parent_category=category2)

#         expected1 = 'category1'
#         self.assertEqual(category1.__str__(), expected1)

#         expected2 = 'category1 - category2'
#         self.assertEqual(category2.__str__(), expected2)

#         expected3 = 'category1 - category2 - category3'
#         self.assertEqual(category3.__str__(), expected3)
