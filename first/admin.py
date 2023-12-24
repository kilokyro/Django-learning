from django.contrib import admin

from first.models import Comment, Post, Tag

# Register your models here.


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_public")
    search_fields = ("title", "content")
    list_filter = ("is_public", "is_draft", "tags")
    filter_horizontal = ("tags",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
