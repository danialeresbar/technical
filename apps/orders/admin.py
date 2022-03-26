from django.contrib import admin

from apps.orders.models import Driver, Order


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
