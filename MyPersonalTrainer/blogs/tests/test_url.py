from unittest.mock import patch

from django.test import TestCase
from django.urls import resolve, reverse

from blogs.views import (
    blogs_view,
    blog_detail_view
)


class TestUrl(TestCase):
    
    def test_blogs_view_function(self):
        resolver = resolve(reverse('blogs_view'))
        self.assertEqual(resolver.func, blogs_view)

    def test_blog_detail_view_function(self):
        resolver = resolve(reverse('blog_detail', args={"slug": "a-slug"}))
        self.assertEqual(resolver.func, blog_detail_view)