from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from .utils import update_vendor_performance

@receiver(post_save, sender=PurchaseOrder)
def update_metrics(sender, instance, **kwargs):
    update_vendor_performance(instance.vendor)
