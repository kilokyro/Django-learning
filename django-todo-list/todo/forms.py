from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = "__all__"
        fields = (
            "title",
            "content",
            "status",
            "project",
            "tags",
        )


class TaskDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="Make sure you wanna CLEAN YOUR ASSS!!!!",
    )
