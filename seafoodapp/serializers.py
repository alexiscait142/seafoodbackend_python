from rest_framework import serializers
from . models import Fish, Region

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = (
            'name', 
            'scientific_name', 
            'biology',
            'location',
            'image',
            'population',
            'harvest',
            'harvest_type',
            'best_harvest',
            'farming_methods',
            'fishing_rate',
            'availability',
            'health_benefits'
            )

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name',)