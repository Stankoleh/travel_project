from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .unit_of_work import UnitOfWork
from .serializers import CountrySerializer, ClientSerializer, JourneySerializer

class CountryListCreateApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        with UnitOfWork() as uow:
            countries = uow.countries.get_all()
            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            with UnitOfWork() as uow:
                country = serializer.save()
                uow.countries.add(country)
                uow.commit()
                return Response(CountrySerializer(country).data, status=201)
        return Response(serializer.errors, status=400)


class CountryRetrieveUpdateDeleteApiView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        with UnitOfWork() as uow:
            country = uow.countries.get_by_id(pk)
            if not country:
                return Response({"error": "Country not found"}, status=404)
            return Response(CountrySerializer(country).data)

    def put(self, request, pk):
        with UnitOfWork() as uow:
            country = uow.countries.get_by_id(pk)
            if not country:
                return Response({"error": "Country not found"}, status=404)

            serializer = CountrySerializer(country, data=request.data)
            if serializer.is_valid():
                updated = serializer.save()
                uow.countries.update(updated)
                uow.commit()
                return Response(CountrySerializer(updated).data)
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        with UnitOfWork() as uow:
            country = uow.countries.get_by_id(pk)
            if not country:
                return Response({"error": "Country not found"}, status=404)
            uow.countries.delete(country)
            uow.commit()
            return Response(status=204)
