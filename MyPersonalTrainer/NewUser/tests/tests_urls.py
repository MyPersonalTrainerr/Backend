from django.test import TestCase
from django.urls import resolve,reverse

from NewUser.views import Login
from rest_auth.registration.views import RegisterView



class TestUrls(TestCase):

    def test_Login_Url(self):
        url=reverse('lgoin')
        self.assertEquals(resolve(url).func.view_class,Login)
    
    def test_Register_Url(self):
        url=reverse('registration')
        self.assertEquals(resolve(url).func.view_class,RegisterView)


