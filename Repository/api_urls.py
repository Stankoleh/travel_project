from django.urls import path
from . import api_views

urlpatterns = [
    # Country
    path('countries/', api_views.CountryApiView.as_view(), name='countries-list'),
    path('countries/<int:pk>/', api_views.CountryApiView.as_view(), name='countries-detail'),

    # Client
    path('clients/', api_views.ClientApiView.as_view(), name='clients-list'),
    path('clients/<int:pk>/', api_views.ClientApiView.as_view(), name='clients-detail'),

    # ContactInfo
    path('contacts/', api_views.ContactInfoApiView.as_view(), name='contacts-list'),
    path('contacts/<int:pk>/', api_views.ContactInfoApiView.as_view(), name='contacts-detail'),

    # Contract
    path('contracts/', api_views.ContractApiView.as_view(), name='contracts-list'),
    path('contracts/<int:pk>/', api_views.ContractApiView.as_view(), name='contracts-detail'),

    # Residence
    path('residences/', api_views.ResidenceApiView.as_view(), name='residences-list'),
    path('residences/<int:pk>/', api_views.ResidenceApiView.as_view(), name='residences-detail'),

    # Transport
    path('transports/', api_views.TransportApiView.as_view(), name='transports-list'),
    path('transports/<int:pk>/', api_views.TransportApiView.as_view(), name='transports-detail'),

    # Journey
    path('journeys/', api_views.JourneyApiView.as_view(), name='journeys-list'),
    path('journeys/<int:pk>/', api_views.JourneyApiView.as_view(), name='journeys-detail'),

    # Aggregated Report
    path('report/', api_views.AggregatedReportApiView.as_view(), name='aggregated-report'),
]
