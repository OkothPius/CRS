from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.urls import reverse


class Log(models.Model):
    case = models.CharField(max_length=100)
    details = models.TextField()
    location = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.case

    # Handles redirect
    def get_absolute_url(self):
        return reverse('post-detail' ,kwargs={'pk': self.pk})
