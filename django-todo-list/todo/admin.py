from django.contrib import admin

from todo.models import Project, Tag, Task

# Register your models here.


@admin.register(Project)
class projectAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class tagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Task)
class taskAdmin(admin.ModelAdmin):
    list_display = ("content", "status")  # "is_finish"
    search_fields = ("title", "content")
    list_filter = ("status", "project", "tags")  # "is_finish"
