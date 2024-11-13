from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),  # Araba detayları için URL

]
