from django import views
from django.urls import path
from .views import CreateTask, TaskDetail, TaskList, UpdateTask

urlpatterns = [
  path('', TaskList.as_view(), name='tasks'),
  path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
  path('create-task/', CreateTask.as_view(), name='create-task'),
  path('update-task/<int:pk>/', UpdateTask.as_view(), name='update-task'),
]