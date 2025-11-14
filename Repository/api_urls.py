from django.urls import path
from .api_views import CountryListCreateApiView, CountryRetrieveUpdateDeleteApiView, ClientListCreateApiView, \
    ClientRetrieveUpdateDeleteApiView

urlpatterns = [
    path('countries/', CountryListCreateApiView.as_view(), name='countries-list'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDeleteApiView.as_view(), name='countries-detail'),
    path('clients/', ClientListCreateApiView.as_view(), name='clients-list'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteApiView.as_view(), name='clients-detail'),

]
