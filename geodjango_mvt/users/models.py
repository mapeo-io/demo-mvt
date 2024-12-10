from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.db import models


class MyUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        validate_password(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractUser):

    USER_TYPES = {
        "sl": "Seller",
        "mg": "Manager"
    }
    username = models.CharField(max_length=64, default="")
    email = models.EmailField(unique=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'type']

    objects = MyUserManager()

    type = models.CharField(max_length=2,
        choices=USER_TYPES,
        default="sl",
    )

    def __str__(self):
        return self.email

    def is_manager(self):
        return self.type == 'mg'
