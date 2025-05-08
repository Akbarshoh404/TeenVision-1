from django.db import models

from django.utils.text import slugify


class Major(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    FORMAT_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('hybrid', 'Hybrid'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male🙋🏻‍♂️'),
        ('female', 'Female🙋🏻‍♀️'),
        ('any', 'Any🙋🏻‍♂️🙋🏻‍♀️'),

    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    desc = models.TextField()
    full_info = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    deadline = models.DateField()
    link = models.URLField()
    country = models.CharField(max_length=100)
    format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    photo = models.ImageField(upload_to='program_photos/', null=True, blank=True)
    type = models.CharField(max_length=100)
    funding = models.CharField(max_length=100)
    start_age = models.PositiveIntegerField()
    end_age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    major = models.ManyToManyField('Major', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
