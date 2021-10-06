from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_dt', 'order_name', 'order_phone')
    list_filter = ('order_dt', 'order_name', 'order_phone')




