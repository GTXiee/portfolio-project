from django.urls import path

from .views import PortfolioPage
from . import views


urlpatterns = [
    path('', PortfolioPage.as_view(), name='portfolio'),
    path('<slug:slug>/', views.job_detail_page, name='job_detail'),
]
