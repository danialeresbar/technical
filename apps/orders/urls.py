from django.urls import path, include
from rest_framework import routers

from apps.orders.views import DriverViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register('drivers', DriverViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
