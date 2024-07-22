from .models import Vendor, PurchaseOrder
from core import models

def update_vendor_performance(vendor):
    completed_orders = vendor.purchase_orders.filter(status='completed')
    total_orders = completed_orders.count()

    if total_orders == 0:
        vendor.on_time_delivery_rate = 0
        vendor.quality_rating_avg = 0
        vendor.average_response_time = 0
        vendor.fulfillment_rate = 0
    else:
        on_time_deliveries = completed_orders.filter(delivery_date__lte=models.F('order_date')).count()
        vendor.on_time_delivery_rate = (on_time_deliveries / total_orders) * 100

        quality_ratings = completed_orders.filter(quality_rating__isnull=False).aggregate(avg=models.Avg('quality_rating'))
        vendor.quality_rating_avg = quality_ratings['avg'] or 0

        response_times = completed_orders.filter(acknowledgment_date__isnull=False).annotate(
            response_time=models.F('acknowledgment_date') - models.F('issue_date')
        ).aggregate(avg=models.Avg('response_time'))
        vendor.average_response_time = response_times['avg'].total_seconds() / 3600 if response_times['avg'] else 0

        vendor.fulfillment_rate = (total_orders / vendor.purchase_orders.count()) * 100

    vendor.save()
