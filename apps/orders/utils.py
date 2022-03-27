from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date, parse_datetime

from apps.orders.models import Driver


def has_pending_orders(driver, date) -> bool:
    for order in driver.orders.all():
        if order.date > date:
            timedelta = order.date - date
            return timedelta.seconds / 3600 <= 1
    return False


def remove_id_from_serialized_data(obj):
    del obj["id"]
    return obj


def euclidean_distance(coordinate_1, coordinate_2) -> float:
    return pow(pow(coordinate_1[0] - coordinate_2[0], 2) + pow(coordinate_1[1] - coordinate_2[1], 2), .5)


def find_nearest_driver(drivers, desired_location):
    nearest_driver = None
    shortest_distance = float('inf')
    for driver in drivers:
        distance = euclidean_distance(driver.get_location(), desired_location)
        if distance <= shortest_distance:
            shortest_distance = distance
            nearest_driver = driver

    return nearest_driver


def validate_date_as_query_param(date, datetime=False):
    validated_date = None
    try:
        validated_date = parse_datetime(date) if datetime else parse_date(date)
    except (TypeError, ValidationError):
        pass

    return validated_date


def validate_driver_as_query_param(driver):
    validated_driver = None
    try:
        validated_driver = Driver.objects.get(pk=driver)
    except (Driver.DoesNotExist, ValueError):
        pass

    return validated_driver


def validate_location_as_query_param(location) -> list:
    validated_location = []
    try:
        validated_location = [int(component) for component in location]
    except ValueError:
        pass
    return validated_location
