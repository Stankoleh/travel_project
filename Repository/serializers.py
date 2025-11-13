from rest_framework import serializers
from .models import Country, Client, Journey

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = "__all__"
