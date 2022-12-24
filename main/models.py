from django.db import models

# Create your models here.
class Samthafs(models.Model):
    images = models.ImageField(null=True, blank=True)