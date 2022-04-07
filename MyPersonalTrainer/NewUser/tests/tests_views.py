from .tests_setup import TestSetUp
from MyPersonalTrainer.settings import AUTH_USER_MODEL as User


class TestViews(TestSetUp):

    def test_user_cannot_register_with_no_data(self):

        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code, 400)

    def test_user_can_register_with_Provided_data(self):

        response = self.client.post(
            self.register_url, self.user_data, formart="json")
        self.assertEquals(response.status_code, 201)

    def test_user_can_login_with_provided_email_and_password(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(
            self.login_url, self.user_data, format="json")
        self.assertEquals(response.status_code, 200)
