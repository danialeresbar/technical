from django.core.validators import MaxValueValidator
from django.db import models

FULL_NAME_MAX_LENGTH = 64
LATITUDE_MAX_LENGTH = 100
LONGITUDE_MAX_LENGTH = 100
COORDINATE_DEFAULT_VALUE = 0


class Driver(models.Model):
    """
    Class used for the representation of the Driver model.The fullname
    attribute is for illustrative purposes because its value is random
    """

    id = models.IntegerField(primary_key=True, editable=False)
    fullname = models.CharField(max_length=FULL_NAME_MAX_LENGTH, default="", null=True, blank=True)
    lat = models.PositiveSmallIntegerField(default=COORDINATE_DEFAULT_VALUE, validators=[MaxValueValidator(LATITUDE_MAX_LENGTH)])
    lng = models.PositiveSmallIntegerField(default=COORDINATE_DEFAULT_VALUE, validators=[MaxValueValidator(LONGITUDE_MAX_LENGTH)])
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"Driver - {self.fullname}"

    def get_location(self) -> list:
        return [self.lat, self.lng]
