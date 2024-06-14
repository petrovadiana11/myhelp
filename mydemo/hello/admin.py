from django.contrib import admin

# Register your models here.
from .models import Employee, Master, Client, Order, Car, Service, HistoryCost, OrderService

# Register your models here.

admin.site.register(Employee)
admin.site.register(Master)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(OrderService)
admin.site.register(HistoryCost)

