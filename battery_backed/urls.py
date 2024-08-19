from django.urls import path
from rest_framework import routers
from .views import StateViewSet

router = routers.DefaultRouter()

router.register(r'state_of_charge', StateViewSet)  # Register your viewsets here


urlpatterns = router.urls