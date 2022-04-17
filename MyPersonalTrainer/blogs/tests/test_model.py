from django.db import models
from django.test import TestCase
from django.contrib.auth import get_user_model

from blogs.models import Post, STATUS


User = get_user_model()

class TestPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            email="someone@somewhere.com",
            username="somehting",
            password="password"
        )

        Post.objects.create(
            title='a post',
            slug='a-post',
            content='something to say',
            author=user
        )

    def test_slug(self):
        post = Post.objects.get(id=1)
        post_test_slug = post._meta.get_field('slug')
        self.assertEqual(post_test_slug.max_length, 128)
        self.assertTrue(post_test_slug.unique)

    def test_title(self):
        post = Post.objects.get(id=1)
        post_title = post._meta.get_field('title')
        self.assertEqual(post_title.max_length, 128)
        self.assertTrue(post_title.unique)

    def test_author(self):
        post = Post.objects.get(id=1)
        post_author = post._meta.get_field('author')
        self.assertTrue(post_author.many_to_one)

    def test_title(self):
        post = Post.objects.get(id=1)
        post_status = post._meta.get_field('status')
        self.assertEqual(post_status.choices, STATUS)
        self.assertEqual(post_status.default, 0)