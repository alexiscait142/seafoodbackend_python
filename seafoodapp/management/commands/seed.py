import os 
import requests
from django.core.management.base import BaseCommand
from ...models import Fish, Region

def get_fishs():
    url = 'https://www.fishwatch.gov/api/species'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    fish = r.json()
    return fish

def get_regions():
    url = 'https://www.fishwatch.gov/api/species'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    fish = r.json()
    all_list = []
    for i in fish:
        if ", " not in i["NOAA Fisheries Region"]:
            all_list.append(i["NOAA Fisheries Region"])
    all_regions = list(set(all_list))
    return all_regions

def clear_data():
    """Deletes all the table data"""
    Fish.objects.all().delete()
    Region.objects.all().delete()

def seed_fish():
    for i in get_fishs():
        fish = Fish(
            name=i["Species Name"],
            scientific_name=i["Scientific Name"],
            biology=i["Biology"],
            location=i["Location"],
            image=i["Species Illustration Photo"]["src"],
            population=i["Population"],
            harvest=i["Harvest"],
            harvest_type=i["Harvest Type"],
            best_harvest=i["Quote"],
            farming_methods=i["Farming Methods"],
            fishing_rate=i["Fishing Rate"],
            availability=i["Availability"],
            health_benefits=i["Health Benefits"],
        )
        fish.save()

def seed_regions():
    for i in get_regions():
        region = Region(
            name=i
        )
        region.save()


seed_fish()
seed_regions()
# clear_data()


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("completed")
