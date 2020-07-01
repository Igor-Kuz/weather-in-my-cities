from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),	# home куда будет возвращать после удаления в views.py
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
]