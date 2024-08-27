from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

  def test_create_user_model(self):
    email = "test@example.com"
    password = "testpass123"

    user = get_user_model().objects.create_user(
      email = email,
      password = password,
    )

    self.assertEqual(user.email,email)
    self.assertTrue(user.check_password(password))
    #check_password basically checks hashed password, and we are hashing our password, during implementation.

  def test_normalized_email(self):
    sample_emails = [
      ['test1@EXAMPLE.com','test1@example.com'],
      ['Test2@Example.com','Test2@example.com'],
      ['TEST3@EXAMPLE.com','TEST3@example.com'],
      ['test4@example.COM','test4@example.com']
    ]

    for email, expected in sample_emails:
      user = get_user_model().objects.create_user(email,'sample123')
      self.assertEqual(user.email,expected)

  def test_raise_value_error_for_blank_email_address(self):
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user('','sample123')

  def test_create_super_user(self):
    email='testsuperuser@example.com'
    password='samplepassword'

    superUser = get_user_model().objects.create_superuser(
      email=email,
      password=password,
    )

    self.assertTrue(superUser.is_superuser)
    self.assertTrue(superUser.is_staff)








