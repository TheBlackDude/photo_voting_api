from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework.authtoken.models import Token

from .models import Account


class AccountModelTestCase(TestCase):

    def get_token(self, username):
        # get users token by passing their username
        try:
            return Token.objects.get(user__username=username).key
        except Exception as e:
            return None

    def test_cannot_create_account_no_data(self):
        account = Account()
        with self.assertRaises(ValidationError):
            account.save()
            account.full_clean()

    def test_cannot_create_account_with_invalid_data(self):
        account = Account(email='me@test.com', first_name='test1')
        with self.assertRaises(ValidationError):
            account.save()
            account.full_clean()

    def test_cannot_create_duplicate_accounts(self):
        account = Account.objects.create(email='me@test.com', username='test')
        account2 = Account(email='me@test.com', username='test')
        with self.assertRaises(IntegrityError):
            account2.save()
            account2.full_clean()

    def test_can_create_user_with_valid_data(self):
        user_details = {'email': 'test@me.com', 'username': 'test',
                        'password': 'test123', 'first_name': 'Test',
                        'last_name': 'Test last'}
        # make sure no user is saved
        self.assertEqual(Account.objects.count(), 0)
        account = Account.objects.create_user(**user_details)

        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(account.first_name, 'Test')

    def test_can_generate_token_if_account_created(self):
        user_details = {'email': 'test@me.com', 'username': 'test',
                        'password': 'test123', 'first_name': 'Test',
                        'last_name': 'Test last'}
        # token doesn't exist yet
        self.assertFalse(self.get_token('test'))

        account = Account.objects.create_user(**user_details)
        self.assertTrue(self.get_token('test')) # now token exist
        user = Token.objects.get(key=self.get_token('test')).user
        self.assertEqual(user.first_name, account.first_name)
