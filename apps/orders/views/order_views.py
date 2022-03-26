from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.orders.models import Driver, Order
from apps.orders.serializers import OrderSerializer
from apps.orders import utils


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], name="schedule_order")
    def schedule_order(self, request):
        serializer = self.get_serializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            scheduled_order = serializer.data
            del scheduled_order["id"]
            return Response(scheduled_order, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], name="orders_by_date")
    def orders_by_date(self, request):
        """

        """

        date = request.query_params.get("date")
        filtered_orders = self.get_queryset().filter(date=date)
        if filtered_orders.exists():
            serializer = self.get_serializer(filtered_orders, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response([], status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], name="orders_by_driver_and_date")
    def orders_by_driver_and_date(self, request):
        """

        """

        date = utils.validate_date_as_query_param(request.query_params.get("date"))
        if date is None:
            return Response(
                {
                    "date": ["This value is mandatory and must be in a valid format"]
                },
                status.HTTP_400_BAD_REQUEST
            )
        driver = utils.validate_driver_as_query_param(request.query_params.get("driver"))
        if driver is None:
            return Response(
                {
                    "driver": ["Ensure this value is a valid driver id"]
                },
                status.HTTP_400_BAD_REQUEST
            )
        filtered_orders = self.get_queryset().filter(driver=driver, date__gte=date)
        if filtered_orders.exists():
            serializer = self.get_serializer(filtered_orders, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response([], status.HTTP_404_NOT_FOUND)


