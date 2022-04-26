from rest_framework.test import APITestCase

from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.login_url = reverse('lgoin')
        self.register_url = reverse('registration')

        self.user_data = {
            'username': "awatef",
            'email': "awatef3@gmail.com",
            'password1': "awatef@gmail",
            'password2': "awatef@gmail",
            'password': "awatef@gmail",
        }

        return super().setUp()
