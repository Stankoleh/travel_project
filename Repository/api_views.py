from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .unit_of_work import UnitOfWork
from .serializers import (
    CountrySerializer, ClientSerializer, ContactInfoSerializer,
    ContractSerializer, ResidenceSerializer, TransportSerializer,
    JourneySerializer
)

class APIViewG(APIView):
    serializer_class = None
    repository_attr = None

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_uow_repo(self):
        uow = UnitOfWork()
        return uow, getattr(uow, self.repository_attr)

    def get(self, request, pk=None):
        uow, repo = self.get_uow_repo()
        if pk:
            obj = repo.get_by_id(pk)
            if not obj:
                return Response({"error": "Not found"}, status=404)
            return Response(self.serializer_class(obj).data)
        objs = repo.get_all()
        return Response(self.serializer_class(objs, many=True).data)

    def update(self, request, pk):
        uow, repo = self.get_uow_repo()
        obj = repo.get_by_id(pk)
        if not obj:
            return Response({"error": "Not found"}, status=404)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            updated = serializer.save()
            repo.update(updated)
            uow.commit()
            return Response(self.serializer_class(updated).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        uow, repo = self.get_uow_repo()
        obj = repo.get_by_id(pk)
        if not obj:
            return Response({"error": "Not found"}, status=404)
        repo.delete(obj)
        uow.commit()
        return Response(status=204)


class CountryApiView(APIViewG):
    serializer_class = CountrySerializer
    repository_attr = 'countries'

class ClientApiView(APIViewG):
    serializer_class = ClientSerializer
    repository_attr = 'clients'

class ContactInfoApiView(APIViewG):
    serializer_class = ContactInfoSerializer
    repository_attr = 'contacts'

class ContractApiView(APIViewG):
    serializer_class = ContractSerializer
    repository_attr = 'contracts'

class ResidenceApiView(APIViewG):
    serializer_class = ResidenceSerializer
    repository_attr = 'residences'

class TransportApiView(APIViewG):
    serializer_class = TransportSerializer
    repository_attr = 'transports'

class JourneyApiView(APIViewG):
    serializer_class = JourneySerializer
    repository_attr = 'journeys'

class AggregatedReportApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        with UnitOfWork() as uow:
            clients_with_journeys = (
                uow.clients.get_all()
                .filter(journeys__isnull=False)
                .distinct()
                .count()
                )

            journeys_with_country = (
                    uow.journeys.get_all()
                    .select_related("country")
                    .count()
                )

            contracts_with_clients = (
                    uow.contracts.get_all()
                    .select_related("client")
                    .count()
                )

            active_residences = (
                uow.residences.get_all()
                .select_related("country")
                .filter(occupied=False)
                .count()
                )

            report = {
                "total_countries": uow.countries.get_all().count(),
                "total_clients": uow.clients.get_all().count(),
                "clients_with_journeys": clients_with_journeys,
                "journeys_with_country": journeys_with_country,
                "contracts_with_clients": contracts_with_clients,
                "active_residences": active_residences,
            }
            return Response(report)
