from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    rating = models.FloatField(default=5.0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.continent})"

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passport = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.passport})"

class ContactInfo(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Contact for {self.client}"



class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Contract {self.contract_number} for {self.client.passport}"


class Residence(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    stars = models.CharField(max_length=10)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.stars} residence at {self.address}"


class Transport(models.Model):
    name = models.CharField(max_length=50)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    direction = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="scheduled")

    def __str__(self):
        return f"{self.name} ({self.status})"


class Journey(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, related_name='journeys')
    address = models.CharField(max_length=200)
    stars = models.CharField(max_length=10)
    transport = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    direction = models.CharField(max_length=20)
    excursions = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)
