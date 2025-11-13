
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/',views.complete_task,name='complete_task'),
    path('task/<int:task_id>/', views.detail_task, name='detail_task')
]
