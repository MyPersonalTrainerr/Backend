from urllib import response

from django.test import TestCase, Client
from django.urls import reverse, resolve

from home.views import Home, SignUp


class URLTest(TestCase):

    def test_HomePage_URL(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, Home)

    def test_SignUp_URL(self):
        url = reverse('SignUp')
        self.assertEquals(resolve(url).func, SignUp)


class ViewsTest(TestCase):

    def test_home_htmlPage(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_SignUpForm(self):
        client = Client()
        response = client.get(reverse('SignUp'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
