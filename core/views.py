from rest_framework import generics,status
from rest_framework.response import Response
from .models import Vendor,PurchaseOrder
from .serializers import VendorSerializer,PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated
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