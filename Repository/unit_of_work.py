from .repositories import (
    CountryRepository, ClientRepository, JourneyRepository,
    ResidenceRepository, TransportRepository, ContractRepository
)

class UnitOfWork:
    countries = CountryRepository()
    clients = ClientRepository()
    journeys = JourneyRepository()
    residences = ResidenceRepository()
    transports = TransportRepository()
    contracts = ContractRepository()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def commit(self):
        pass
