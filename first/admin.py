from django.contrib import admin

from first.models import Post

# Register your models here.


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_public")
    search_fields = ("title", "content")
    list_filter = ("is_public", "is_draft")
