from django.db import models

from django.utils.text import slugify


class Major(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    FORMAT_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Oflayn'),
        ('hybrid', 'Gibrid'),
    ]

    GENDER_CHOICES = [
        ('male', 'Erkaklar uchun'),
        ('female', 'Ayollar uchun'),
        ('any', 'Hamma uchun'),
    ]

    FUNDING_CHOICES = [
        ('full', "To'liq moliyalashtiriladi"),
        ('partial', 'Qisman moliyalashtiriladi'),
        ('self', "O'zi to'laydi"),
        ('sponsorship', 'Sponsorlik orqali'),
    ]

    TYPE_CHOICES = [
        ('program', 'Dastur'),
        ('tutorial', 'Tutorial'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    full_info = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    link = models.URLField()
    country = models.CharField(max_length=100, null=True, blank=True)
    format = models.CharField(max_length=50, choices=FORMAT_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to='program_photos/', null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    funding = models.CharField(max_length=100, choices=FUNDING_CHOICES, null=True, blank=True)
    start_age = models.PositiveIntegerField(null=True, blank=True)
    end_age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    major = models.ManyToManyField('Major', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.type == 'tutorial':
            self.desc = None
            self.full_info = None
            self.deadline = None
            self.country = None
            self.format = None
            self.photo = None
            self.funding = None
            self.start_age = None
            self.end_age = None
            self.gender = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
