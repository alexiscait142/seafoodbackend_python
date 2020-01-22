from django.db import models

# Create your models here.


class Fish(models.Model):
    name=models.CharField(max_length=2000, blank=True, null=True)
    scientific_name=models.CharField(max_length=2000, blank=True, null=True)
    biology=models.CharField(max_length=2000, blank=True, null=True)
    location=models.CharField(max_length=2000, blank=True, null=True)
    image=models.CharField(max_length=2000, blank=True, null=True)
    population=models.CharField(max_length=2000, blank=True, null=True)
    harvest=models.CharField(max_length=2000, blank=True, null=True)
    harvest_type=models.CharField(max_length=2000, blank=True, null=True)
    best_harvest=models.CharField(max_length=2000, blank=True, null=True)
    farming_methods=models.CharField(max_length=2000, blank=True, null=True)
    fishing_rate=models.CharField(max_length=2000, blank=True, null=True)
    availability=models.CharField(max_length=2000, blank=True, null=True)
    health_benefits=models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
