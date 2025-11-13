from django.contrib import admin
from .models import Country, Client, ContactInfo, Contract, Residence, Transport, Journey

admin.site.register(Country)
admin.site.register(Client)
admin.site.register(ContactInfo)
admin.site.register(Contract)
admin.site.register(Residence)
admin.site.register(Transport)
admin.site.register(Journey)

