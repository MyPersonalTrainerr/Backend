from django.test import TestCase
from django.urls import resolve
from blogs.views import blogs_view


class TestUrl(TestCase):
    def test_blog_view_function(self):
        resolver = resolve('/blogs')
        self.assertEqual(resolver.func, blogs_view)