from django.test import TestCase
from api.models import Tag


class ModelTests(TestCase):

    def test_retrieve_recursd_tag_name(self):
        tag1 = Tag.objects.create(name='Tag1')
        tag2 = Tag.objects.create(name='Tag2', parent_tag=tag1)
        tag3 = Tag.objects.create(name='Tag3', parent_tag=tag2)

        expected1 = 'Tag1'
        self.assertEqual(tag1.__str__(), expected1)

        expected2 = 'Tag1 - Tag2'
        self.assertEqual(tag2.__str__(), expected2)

        expected3 = 'Tag1 - Tag2 - Tag3'
        self.assertEqual(tag3.__str__(), expected3)
