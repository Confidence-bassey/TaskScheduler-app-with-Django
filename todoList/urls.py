from django.urls import path
from . import views



urlpatterns = [
    path('', views.task_list, name='list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/add/', views.task_create, name='create-task'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('auth/register/', views.register, name='register'),


]