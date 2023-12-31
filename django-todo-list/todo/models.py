from django.db import models


# Create your models here.
class Project(models.Model):
    class Status(models.TextChoices):
        Planning = "P", "Planning"
        Block = "B", "Block"
        Doing = "D", "Doing"
        Finish = "F", "Finish"

    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.Planning,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_finish = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="tasks")
    tags = models.ManyToManyField("Tag", blank=True, related_name="projects")

    def __str__(self):
        return self.content
