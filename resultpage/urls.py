from django.urls import path
from . import views

app_name = 'resultpage'

urlpatterns = [
    path('', views.completed_job_list, name='completed_job_list'),
]