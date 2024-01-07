from django.urls import path

from todo.views import task_create, task_delete, task_list, task_retrieve, task_update

app_name = "todo"

urlpatterns = [
    path("tasks/", task_list, name="task_list"),
    path("tasks/create/", task_create, name="task_create"),
    path("tasks/<int:pk>", task_retrieve, name="task_retrieve"),
    path("tasks/<int:pk>/update/", task_update, name="task_update"),
    path("tasks/<int:pk>/delete/", task_delete, name="task_delete"),
]
