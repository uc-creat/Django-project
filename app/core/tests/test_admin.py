from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


# prepare the setup. setUp - should be named as such only

class AdminSiteTests(TestCase):
  def setUp(self) -> None:
    #create a superuser and force login it.
    self.admin_user = get_user_model().objects.create_superuser(
      email='admin@example.com',
      password='anypassword'
    )
    # force login
    self.client = Client()
    self.client.force_login(self.admin_user)

    self.user = get_user_model().objects.create_user(
      email='user@example.com',
      password='user123',
      name = 'Test User'
    )

  def test_users_list(self):
    url = reverse('admin:core_user_changelist')
    res = self.client.get(url)

    self.assertContains(res, self.user.email)
    self.assertContains(res, self.user.name)

  def test_user_detail_page(self):
    url = reverse('admin:core_user_change',args=[self.user.id])
    res = self.client.get(url)

    self.assertEqual(res.status_code,200)
    # just checking if the page loads successfully

  def test_create_user_page(self):
    url = reverse('admin:core_user_add')
    res = self.client.get(url)

    self.assertEqual(res.status_code,200)


