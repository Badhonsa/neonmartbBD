from django.db import models
from django.contrib.auth.models import User


class work(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'

