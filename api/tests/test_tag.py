from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from api.models import Tag

TAG_URL = reverse('api:tag-list')


def detail_url(tag_id):
    return reverse('api:tag-detail', args=[tag_id])


def sample_tag(user, **params):
    """
    Create and return a sample of tag
    """
    defaults = {
        'name': 'test_tag',
    }
    defaults.update(params)

    return Tag.objects.create(user=user, **defaults)


class PublicTestCase(TestCase):
    """
    Test for publicy avaialable tag API
    """

    def setUp(self):

        self.client = APIClient()

    def test_login_required(self):
        """
        Tests if login is required for retriving tags
        """

        res = self.client.get(TAG_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTestCase(TestCase):
    """
    Test for private tag API
    """

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            'testuser',
            'supertest'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_login_required_ok(self):
        """
        Test retriving tags for logged in user
        """

        Tag.objects.create(
            user=self.user,
            name='test'
        )
        res = self.client.get(TAG_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_getting_all_tags(self):
        """
        Test getting all tags
        """

        Tag.objects.create(
            user=self.user,
            name='test'
        )
        Tag.objects.create(
            user=self.user,
            name='test2'
        )
        res = self.client.get(TAG_URL)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['name'], 'test')
        self.assertEqual(res.data[1]['name'], 'test2')

    def test_getting_single_tag(self):
        """
        Testing getting single tag
        """

        sample_tag(self.user)
        tag2 = sample_tag(
            self.user,
            name='food')

        url = detail_url(tag2.id)
        res = self.client.get(url)

        self.assertFalse(isinstance(res.data, list))
        self.assertEqual(res.data['name'], 'food')

    def test_getting_tags_assined_to_user(self):
        """
        Test filtering tags for logged user
        """

        self.user2 = get_user_model().objects.create_user(
            'testuser2',
            'supertest'
        )

        sample_tag(self.user, name='food')
        sample_tag(self.user2, name='transport')

        res = self.client.get(TAG_URL)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], 'food')
