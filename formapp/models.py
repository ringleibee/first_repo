from django.db import models

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()