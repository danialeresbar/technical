import names
import requests

from django.db.utils import IntegrityError
from django.core.management import BaseCommand

from apps.orders.models import Driver

DRIVERS_URL = "https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json"


class Command(BaseCommand):

    def handle(self, *args, **options):
        incoming_drivers = list()
        response = requests.get(DRIVERS_URL).json()
        alfred_drivers = response.get("alfreds", list())

        for driver in alfred_drivers:
            incoming_drivers.append({
                "id": driver.get("id"),
                "fullname": names.get_full_name(),
                "lat": driver.get("lat"),
                "lng": driver.get("lng"),
                "updated_at": driver.get("lastUpdate")
            })

        try:
            # First time
            Driver.objects.bulk_create(
                [Driver(**driver) for driver in incoming_drivers]
            )
        except IntegrityError:
            current_drivers = Driver.objects.filter(id__in=[driver[id] for driver in incoming_drivers])
            # TODO: Update the current_drivers
            pass

