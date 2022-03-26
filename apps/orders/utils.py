from django.utils.dateparse import parse_date

from apps.orders.models import Driver


def validate_date_as_query_param(date):
    validated_date = None
    try:
        validated_date = parse_date(date)
    except TypeError:
        pass

    return validated_date


def validate_driver_as_query_param(driver):
    validated_driver = None
    try:
        validated_driver = Driver.objects.get(pk=driver)
    except (Driver.DoesNotExist, ValueError):
        pass

    return validated_driver


def find_nearest_driver(drivers, desired_location):
    pass
