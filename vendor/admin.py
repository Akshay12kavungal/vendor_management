from django.contrib import admin
from .models import Vendor, PurchaseOrder

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ('name', 'vendor_code')
    list_filter = ('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'status', 'quality_rating')
    search_fields = ('po_number', 'vendor__name')
    list_filter = ('status', 'order_date', 'delivery_date')
