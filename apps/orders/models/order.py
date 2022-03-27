from django.core.validators import MaxValueValidator
from django.db import models

from apps.orders.models import Driver

DRIVER_RELATED_NAME = "orders"
LATITUDE_MAX_LENGTH = 100
LONGITUDE_MAX_LENGTH = 100
COORDINATE_DEFAULT_VALUE = 0


class Order(models.Model):
    """
    Class used for the representation of the Order model
    """

    driver = models.ForeignKey(Driver, related_name=DRIVER_RELATED_NAME, on_delete=models.CASCADE)
    date = models.DateTimeField()
    pickup_lat = models.PositiveSmallIntegerField(
        default=COORDINATE_DEFAULT_VALUE,
        validators=[MaxValueValidator(LATITUDE_MAX_LENGTH)]
    )
    pickup_lng = models.PositiveSmallIntegerField(
        default=COORDINATE_DEFAULT_VALUE,
        validators=[MaxValueValidator(LONGITUDE_MAX_LENGTH)]
    )
    destination_lat = models.PositiveSmallIntegerField(
        default=COORDINATE_DEFAULT_VALUE,
        validators=[MaxValueValidator(LATITUDE_MAX_LENGTH)]
    )
    destination_lng = models.PositiveSmallIntegerField(
        default=COORDINATE_DEFAULT_VALUE,
        validators=[MaxValueValidator(LONGITUDE_MAX_LENGTH)]
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order - {self.driver} from [{self.pickup_lat},{self.pickup_lng}] to [{self.destination_lat}, {self.destination_lng}]"
