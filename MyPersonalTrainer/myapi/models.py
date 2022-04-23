from django.db import models

# Create your models here.
class file(models.Model):
    path=models.CharField(max_length=1000)
    progress=progress=models.IntegerField(default=0)