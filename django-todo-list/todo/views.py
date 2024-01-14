from django.contrib import messages
from django.contrib.auth import decorators as auth_decorators
from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import TaskDeleteConfirmForm, TaskForm
from todo.models import Task

# Create your views here.


def task_list(request):
    if not request.user.is_authenticated:
        messages.info(request, "Login to have access to more functions!")

    tasks = Task.objects.select_related("project").prefetch_related("tags")
    request.session["BBB"] = "CCC"

    response = render(request, "todo/task_list.html", {"tasks": tasks})
    response.set_cookie("AAA", "BBB")
    return response

    # return render(
    #     request,
    #     "todo/task_list.html",
    #     {"tasks": tasks},
    # )


@auth_decorators.login_required
def task_create(request):
    print(request.session.get("BBB"))
    print(request.COOKIES)
    form = TaskForm(request.POST or None)
    if form.is_valid():
        # post = Post.objects.create(**form.cleaned_data)
        task = form.save()
        messages.success(request, "Create Success")
        return redirect("task_retrieve", pk=task.pk)

    return render(
        request,
        "todo/task_create.html",
        {"form": form},
    )


def task_retrieve(request, pk):
    task = get_object_or_404(Task.objects.prefetch_related("tags"), pk=pk)
    return render(
        request,
        "todo/task_retrieve.html",
        {"task": task},
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save()
        messages.success(request, "Update Success")
        return redirect("task_retrieve", pk=task.pk)

    return render(
        request,
        "todo/task_update.html",
        {"form": form},
    )


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        task.delete()
        messages.success(request, "Delete Success")
        return redirect("task_list")

    return render(
        request,
        "todo/task_delete.html",
        {"form": form},
    )
