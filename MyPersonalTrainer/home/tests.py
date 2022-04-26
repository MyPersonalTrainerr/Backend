from urllib import response

from django.test import TestCase, Client
from django.urls import reverse, resolve

from home.views import Home


class URLTest(TestCase):

    def test_HomePage_URL(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, Home)


class ViewsTest(TestCase):

    def test_home_htmlPage(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
