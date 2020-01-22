from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fishs', views.FishView)
router.register('regions', views.RegionView)

urlpatterns = [
    path('', include(router.urls))
]