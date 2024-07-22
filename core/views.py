from rest_framework import generics,status
from rest_framework.response import Response
from .models import Vendor,PurchaseOrder
from .serializers import VendorSerializer,PurchaseOrderSerializer
# Create your views here.



class VendorListCreateView(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer


class VendorRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


    def get_queryset(self):
        vendor_id=self.request.query_params.get('vendor_id')
        if vendor_id:
            return self.queryset.filter(vendor_id=vendor_id)
        return super().get_queryset()



class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        performance_data={

            "on_time_delivery_rate": instance.on_time_delivery_rate,
            "quality_rating_avg": instance.quality_rating_avg,
            "average_response_time": instance.average_response_time,
            "fulfillment_rate": instance.fulfillment_rate,

        }
        return Response(performance_data)