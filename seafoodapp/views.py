from django.shortcuts import render
from rest_framework import viewsets
from . models import Fish, Region
from . serializers import FishSerializer, RegionSerializer
import requests

# Create your views here.

class FishView(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer