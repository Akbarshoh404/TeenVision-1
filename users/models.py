from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

from .managers import UserManager
from core.models import Program


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    GENDER_CHOICES = [
        ('male', 'Male🙋🏻‍♂️'),
        ('female', 'Female🙋🏻‍♀️'),
    ]

    username = None  # Username o‘chiriladi, email orqali login
    email = models.EmailField(unique=True)

    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    country = models.CharField(max_length=100, default='Uzb', null=True, blank=True)
    liked_programs = models.ManyToManyField(Program, blank=True, related_name='liked_by_users')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # ismingiz, familiyangiz talab qilinadi

    def __str__(self):
        return self.email

    def is_user(self):
        return self.role == 'user'

    def is_admin(self):
        return self.role == 'admin'
