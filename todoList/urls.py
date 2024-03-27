from django.urls import path
from . import views

app_name = 'todoList'

urlpatterns = [
    path('task/list/', views.task_list, name='list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/add/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/add/accounts/login/', views.task_create, name='task_create'),
    path('task/add/accounts/register/', views.register, name='register'),
    path('register/', views.register, name='register'),


]