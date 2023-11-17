from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.user_homepage, name="user_homepage"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("add-task", views.add_task, name="add_task"),
    path("task-list", views.task_list, name="task_list")

]