from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.orders.models import Driver
from apps.orders.serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'], name="locate_driver")
    def locate_driver(self, request):
        desired_lat = request.query_params.get("lat")
        desired_lng = request.query_params.get("lng")
        drivers = self.get_queryset().filter()
        return Response([desired_lat, desired_lng], status.HTTP_200_OK)
