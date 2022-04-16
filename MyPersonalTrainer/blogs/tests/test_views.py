from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):
    def test_blog_view_function(self):
        response = self.client.get(reverse('blogs_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blogs.html')