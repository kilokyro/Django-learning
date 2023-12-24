"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from first.views import (
    create_post,
    delete_post,
    get_post,
    hello_world,
    list_item,
    list_post,
    repeat,
    say_hello,
    say_hi,
    update_post,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", hello_world),
    path("say-hello/", say_hello),
    path("repeat/<str:content>/<int:times>/", repeat),
    path("list-item/<str:item>/<int:times>/", list_item),
    path("say-hi/", say_hi),
    path("posts/", list_post, name="list_post"),
    path("posts/<int:pk>/", get_post, name="get_post"),
    path("posts/create/", create_post, name="create_post"),
    path("posts/<int:pk>/update/", update_post, name="update_post"),
    path("posts/<int:pk>/delete/", delete_post, name="delete_post"),
]
