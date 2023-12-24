from django import forms

from first.models import Post

"""
class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ("title","author", "is_public")
        # fields = "__all__"
        exclude = ("is_public",)


class PostDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="Make sure you wanna CLEAN YOUR ASSS!!!!",
    )
