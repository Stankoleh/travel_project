from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.list_countries, name='list_countries'),
    path('clients/', views.list_clients, name='list_clients'),
    path('journeys/', views.list_journeys, name='list_journeys'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
]
