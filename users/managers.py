from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email kiritilishi shart!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class AdminManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email kiritilishi shart!')
        email = self.normalize_email(email)
        admin = self.model(email=email, is_staff=True, is_superuser=True, **extra_fields)
        admin.set_password(password)
        admin.save()
        return admin

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email=email, password=password, **extra_fields)

