from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from blogs.models import Post

User = get_user_model()


class TestView(TestCase):
    def test_blogs_view_function(self):
        response = self.client.get(reverse('blogs_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blogs.html')

    def test_blog_detail_view_function(self):
        user = User.objects.create_user(
            email="someone@somewhere.com",
            username="somehting",
            password="password"
        )

        post = Post.objects.create(
            title='a post',
            slug='a-post',
            content='something to say',
            author=user
        )

        response = self.client.get(reverse('blog_detail', kwargs={"slug": post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_detail.html')