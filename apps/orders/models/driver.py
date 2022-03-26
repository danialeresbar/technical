from django.core.validators import MaxValueValidator
from django.db import models

FULL_NAME_MAX_LENGTH = 64


class Driver(models.Model):
    """

    """

    id = models.IntegerField(primary_key=True, editable=False)
    fullname = models.CharField(max_length=FULL_NAME_MAX_LENGTH, default="", null=True, blank=True)
    lat = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    lng = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"Driver - {self.fullname}"

    def get_location(self) -> list:
        """

        """

        return [self.lat, self.lng]
