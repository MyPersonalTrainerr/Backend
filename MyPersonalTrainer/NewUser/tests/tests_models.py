from django.test import TestCase
from NewUser.models import Account


class TestModels(TestCase):
    def test_value_error_of_empty_email(self):
        with self.assertRaises(ValueError):
            User_Data = Account.objects.create_user(
                email='',
                username='awatef',
                password='123456789'
            )

    def test_value_error_of_empty_username(self):
        with self.assertRaises(ValueError):
            User_Data = Account.objects.create_user(
                email='awatef@gamil.com',
                username='',
                password='123456789'
            )

    def test_save_user(self):
        user = Account.objects.create_user(
            email='awatef@gmail.com',
            username='awatef',
            password='123456'
        )
        
        self.assertTrue(isinstance(user, Account))
        self.assertEquals(Account.__str__(user), 'awatef@gmail.com')
        self.assertEquals(Account.has_perm(user), user.is_admin)
        self.assertEquals(Account.has_module_perms(user), True)

    def test_save_superuser(self):
        user = Account.objects.create_superuser(
            email='awatef@gmail.com',
            username='awatef',
            password='123456'
        )

        self.assertTrue(isinstance(user, Account))
        self.assertEquals(Account.__str__(user), 'awatef@gmail.com')
        self.assertEquals(Account.has_perm(user), user.is_admin)
        self.assertTrue(Account.has_module_perms(user))
        
