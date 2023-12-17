from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
