from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
]
