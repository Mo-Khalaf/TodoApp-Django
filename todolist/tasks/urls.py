from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index ,name='list'),
    path('updated_task/<str:pk>', views.UpdateTask, name='update_task'),
    path('delete_task/<str:pk>', views.DeleteTask, name='delete_task'),
]

