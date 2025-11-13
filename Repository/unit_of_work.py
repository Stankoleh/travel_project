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
