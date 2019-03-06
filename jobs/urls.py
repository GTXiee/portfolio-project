from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
]
