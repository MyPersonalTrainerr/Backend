from django.db import models
from NewUser.models import Account


class File(models.Model):
    Path = models.CharField(max_length=1000)
    UserProfile = models.ForeignKey(
        Account, on_delete=models.CASCADE)
