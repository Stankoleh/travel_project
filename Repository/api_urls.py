from django.urls import path
from .api_views import CountryListCreateApiView, CountryRetrieveUpdateDeleteApiView

urlpatterns = [
    path('countries/', CountryListCreateApiView.as_view(), name='countries-list'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDeleteApiView.as_view(), name='countries-detail'),

]
