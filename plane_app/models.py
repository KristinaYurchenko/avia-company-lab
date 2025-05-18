from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airplanes')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, related_name='airplanes')
    year_produced = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} ({self.airline.name})"
