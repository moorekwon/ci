# Create your tests here.
from django.test import TestCase


class BlogTest(TestCase):
    def test_post_list(self):
        response = self.client.get('/posts/')