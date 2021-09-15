from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Log(models.Model):
    case = models.CharField(max_length=100)
    details = models.TextField()
    location = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    num_reported = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.case} in {self.location}'

    # Handles redirect
    def get_absolute_url(self):
        return reverse('log-home')
