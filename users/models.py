from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

from .managers import UserManager, AdminManager
from core.models import Program


class User(AbstractUser):
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

    groups = models.ManyToManyField(Group, related_name='user_groups_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # ismingiz, familiyangiz talab qilinadi

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AdminUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name='adminuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='adminuser_permissions', blank=True)

    objects = AdminManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
