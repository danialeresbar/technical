from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.orders.models import Driver
from apps.orders.serializers import DriverSerializer
from apps.orders import utils


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'], name="locate_driver")
    def locate_driver(self, request):
        date = utils.validate_date_as_query_param(request.query_params.get("date"), datetime=True)
        if date is None:
            return Response(
                {
                    "date": ["This query parameter is mandatory and must be in a valid format. It must be in YYYY-MM-DD HH:MM"]
                },
                status.HTTP_400_BAD_REQUEST
            )

        desired_location = utils.validate_location_as_query_param(
            location=[request.query_params.get("lat"), request.query_params.get("lng")]
        )
        if not desired_location:
            return Response(
                {
                    "lat": ["Ensure this value is less than or equal to 100"],
                    "lng": ["Ensure this value is less than or equal to 100"]
                },
                status.HTTP_400_BAD_REQUEST
            )
        filtered_drivers = self.get_queryset().filter(updated_at=date)
        driver = utils.find_nearest_driver(drivers=filtered_drivers, desired_location=desired_location)
        if utils.has_pending_orders(driver, date):
            return Response({}, status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.get_serializer(driver, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
