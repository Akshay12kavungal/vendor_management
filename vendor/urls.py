from django.urls import path
from .views import (
    VendorListView, VendorDetailView, VendorCreateView, VendorUpdateView, VendorDeleteView,
    PurchaseOrderListView, PurchaseOrderDetailView, PurchaseOrderCreateView, PurchaseOrderUpdateView, PurchaseOrderDeleteView,
    VendorPerformanceView
)

urlpatterns = [
    path('', VendorListView.as_view(), name='vendor_list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor_detail'),
    path('vendors/create/', VendorCreateView.as_view(), name='vendor_create'),
    path('vendors/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor_update'),
    path('vendors/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
    
    path('purchase_orders/', PurchaseOrderListView.as_view(), name='purchase_order_list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase_order_detail'),
    path('purchase_orders/create/', PurchaseOrderCreateView.as_view(), name='purchase_order_create'),
    path('purchase_orders/<int:pk>/update/', PurchaseOrderUpdateView.as_view(), name='purchase_order_update'),
    path('purchase_orders/<int:pk>/delete/', PurchaseOrderDeleteView.as_view(), name='purchase_order_delete'),
]
