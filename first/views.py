from django.http import HttpResponse
from django.shortcuts import render

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
        {"posts": posts},
    )
