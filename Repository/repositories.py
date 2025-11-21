from .models import Country, Client, Journey, Residence, Transport, Contract

class CountryRepository:
    def get_all(self):
        return Country.objects.all()

    def get_by_id(self, country_id):
        return Country.objects.filter(id=country_id).first()

    def add(self, country):
        country.save()

    def update(self, country):
        country.save()

    def delete(self, country):
        country.delete()

class ClientRepository:
    def get_all(self):
        return Client.objects.all()

    def get_by_id(self, client_id):
        return Client.objects.filter(id=client_id).first()

    def add(self, client):
        client.save()

    def update(self, client):
        client.save()

    def delete(self, client):
        client.delete()

class JourneyRepository:
    def get_all(self):
        return Journey.objects.prefetch_related('clients', 'country').all()

    def get_by_id(self, journey_id):
        return Journey.objects.filter(id=journey_id).first()

    def add(self, journey):
        journey.save()


class ResidenceRepository:
    def get_all(self):
        return Residence.objects.select_related('country').all()

    def add(self, residence):
        residence.save()


class TransportRepository:
    def get_all(self):
        return Transport.objects.all()

    def add(self, transport):
        transport.save()


class ContractRepository:
    def get_all(self):
        return Contract.objects.select_related('client').all()

    def add(self, contract):
        contract.save()
