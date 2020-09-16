# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model

# from rest_framework import status
# from rest_framework.test import APIClient

# from api.models import Tag

# TAG_URL = reverse('api:tag')


# class PublicTestCase(TestCase):
#     """
#     Test for publicy avaialable tag API
#     """

#     def setUp(self):

#         self.client = APIClient()

#     def test_login_required(self):
#         """
#         Tests if login is required for retriving categories
#         """

#         res = self.client.get(TAG_URL)

#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


# class PrivateTestCase(TestCase):
#     """
#     Test for private tag API
#     """

#     def setUp(self):

#         self.user = get_user_model().objects.create_user(
#             'testuser',
#             'supertest'
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(self.user)

#     def test_creating_tag(self):

#         payload = {
#             'name': 'test',
#             'user_id': self.user.id}

#         tag = self.client.post(TAG_URL, payload)
#         print(tag)
#         response = Tag.objects.get(user=self.user)

#         self.assertEqual(
#             response,
#             self.user.username + ' - ' + payload['name'])

#     def test_test(self):
#         self.assertEqual(1,1)
