from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)


class UserManager(BaseUserManager):
  def create_user(self, email, password = None, **extra_fields):

    # first_part,second_part = email.split("@")
    # normalized_email = first_part + "@"+second_part.lower() - my logic which is correct.

    if not email:
      raise ValueError('Provide a valid email')
    user = self.model(email=self.normalize_email(email),**extra_fields)
    user.set_password(password)
    user.save(self._db)
    return user

  def create_superuser(self, email, password):
    superUser = self.create_user(email,password)
    superUser.is_superuser = True
    superUser.is_staff = True
    superUser.save(using=self._db)
    return superUser

class User(AbstractBaseUser,PermissionsMixin):
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  #overriding the userfield, which is name by default

  objects = UserManager()

  USERNAME_FIELD = 'email'

