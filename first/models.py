from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    is_draft = models.BooleanField(null=True)
    dt = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content


"""
models.PROTECT
models.CASCADE
models.SET_NULL
models.SET_DEFAULT
"""


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
