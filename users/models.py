from django.contrib.auth.models import AbstractUser
from django.db import models

from core.managers import CustomUserManager
from core.models import Program


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male🙋🏻‍♂️'),
        ('female', 'Female🙋🏻‍♀️'),
    ]

    username = None  # Username o‘chiriladi, email orqali login
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, )
    country = models.CharField(max_length=100, default='Uzb')
    liked_programs = models.ManyToManyField(Program, blank=True, related_name='liked_by_users')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # ismingiz, familiyangiz talab qilinadi

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
