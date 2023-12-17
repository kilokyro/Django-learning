from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    is_draft = models.BooleanField(null=True)
    dt = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
