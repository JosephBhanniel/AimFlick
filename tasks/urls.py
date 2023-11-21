from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.user_homepage, name="user_homepage"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("add-task", views.add_task, name="add_task"),
    path("task-list", views.task_list, name="task_list"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("<int:id>", views.task_details, name="task_details"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('completed/<int:id>/', views.completed, name='completed'),
]