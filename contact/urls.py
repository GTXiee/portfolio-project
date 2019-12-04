from django.urls import path

from . import views


urlpatterns = [
    path('', views.contact_page, name='contact'),
    path('thanks/', views.thanks_page, name='thanks'),
]
