from django.test import TestCase
from api.models import Tag
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


class ModelTests(TestCase):



    def setUp(self):

        self.user = get_user_model().objects.create_user(
            'testuser',
            'supertest'
        )
        self.client = APIClient()

    def test_retrieve_recursd_tag_name(self):
        tag1 = Tag.objects.create(name='Tag1',
                                  user=self.user)

        tag2 = Tag.objects.create(name='Tag2',
                                  user=self.user,
                                  parent_tag=tag1)

        tag3 = Tag.objects.create(name='Tag3',
                                  user=self.user,
                                  parent_tag=tag2)

        expected1 = 'Tag1'
        self.assertEqual(tag1.__str__(), expected1)

        expected2 = 'Tag1 - Tag2'
        self.assertEqual(tag2.__str__(), expected2)

        expected3 = 'Tag1 - Tag2 - Tag3'
        self.assertEqual(tag3.__str__(), expected3)
