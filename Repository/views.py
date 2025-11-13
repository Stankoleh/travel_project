from django.shortcuts import render, get_object_or_404
from .unit_of_work import UnitOfWork
from .models import Client

def list_countries(request):
    countries = UnitOfWork.countries.get_all()
    return render(request, 'Repository/countries.html', {'countries': countries})

def list_clients(request):
    clients = UnitOfWork.clients.get_all()
    return render(request, 'Repository/clients.html', {'clients': clients})

def list_journeys(request):
    journeys = UnitOfWork.journeys.get_all()
    return render(request, 'Repository/journeys.html', {'journeys': journeys})

def client_detail(request, client_id):
    client = UnitOfWork.clients.get_by_id(id=client_id)
    return render(request, 'Repository/client_detail.html', {'client': client})
