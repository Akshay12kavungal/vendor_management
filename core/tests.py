from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vendor, PurchaseOrder

class VendorTests(APITestCase):
    def test_create_vendor(self):
        url = reverse('vendor-list-create')
        data = {
            "name": "Vendor 1",
            "contact_details": "Contact details",
            "address": "Address",
            "vendor_code": "V001"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PurchaseOrderTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Vendor 1",
            contact_details="Contact details",
            address="Address",
            vendor_code="V001"
        )

    def test_create_purchase_order(self):
        url = reverse('purchase-order-list-create')
        data = {
            "po_number": "PO001",
            "vendor": self.vendor.id,
            "order_date": "2024-07-22T00:00:00Z",
            "delivery_date": "2024-07-29T00:00:00Z",
            "items": {},
            "quantity": 10,
            "status": "pending"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
