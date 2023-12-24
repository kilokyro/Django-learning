from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from first.forms import PostDeleteConfirmForm, PostForm
from first.models import Post


def hello_world(request):
    return HttpResponse("Test 123, HelloWorld")


def say_hello(request):
    name = request.GET.get("name", "unknown")
    repeat = int(request.GET.get("repeat", "Many"))
    # return HttpResponse(
    #     f" welcome here!{name},\n｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡ Welcome you {repeat*repeat} times!"
    # )
    return render(
        request,
        "first/say_hello.html",
        {"name": name, "range": range(repeat)},
    )


def repeat(request, content, times):
    # return HttpResponse(f"<h1>{content*times}</h1>")
    return render(
        request,
        "first/repeat.html",
        {"Content": content, "Times": times},
    )


def list_item(request, item, times):
    return render(
        request,
        "first/list_item.html",
        {
            "item": item,
            "times": times,
            "range": range(times),
            "show": request.GET.get("show", "") == "true",
        },
    )


def say_hi(request):
    return render(
        request,
        "first/say_hi.html",
        {"name": request.POST.get("name", "123")},
    )


def list_post(request):
    posts = Post.objects.all()
    return render(
        request,
        "first/list_post.html",
        {
            "posts": posts,
            "show": request.GET.get("show", "") == "true",
        },
    )


def get_post(request, pk):
    # post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk)
    return render(
        request,
        "first/get_post.html",
        {
            "post": post,
        },
    )


def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        # post = Post.objects.create(**form.cleaned_data)
        post = form.save()
        messages.success(request, "Create Success")
        return redirect("get_post", pk=post.id)

    return render(
        request,
        "first/create_post.html",
        {"form": form},
    )


def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, "Update Success")
        return redirect("get_post", pk=post.id)

    return render(
        request,
        "first/update_post.html",
        {"form": form},
    )


def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        post.delete()
        messages.success(request, "Delete Success")
        return redirect("list_post")

    return render(
        request,
        "first/delete_post.html",
        {"form": form},
    )
