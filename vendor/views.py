from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Vendor, PurchaseOrder
from .forms import VendorForm, PurchaseOrderForm

# Vendor Views
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'
    context_object_name = 'vendors'

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendors/vendor_detail.html'
    context_object_name = 'vendor'

class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'vendors/vendor_form.html'
    success_url = reverse_lazy('vendor_list')

class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'vendors/vendor_form.html'
    success_url = reverse_lazy('vendor_list')

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'vendors/vendor_confirm_delete.html'
    success_url = reverse_lazy('vendor_list')

# Purchase Order Views
class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'vendors/purchase_order_list.html'
    context_object_name = 'purchase_orders'

class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder
    template_name = 'vendors/purchase_order_detail.html'
    context_object_name = 'purchase_order'

class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'vendors/purchase_order_form.html'
    success_url = reverse_lazy('purchase_order_list')

class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'vendors/purchase_order_form.html'
    success_url = reverse_lazy('purchase_order_list')

class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    template_name = 'vendors/purchase_order_confirm_delete.html'
    success_url = reverse_lazy('purchase_order_list')

# Vendor Performance View
class VendorPerformanceView(TemplateView):
    template_name = 'vendors/vendor_performance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendor_id = self.kwargs.get('vendor_id')
        vendor = Vendor.objects.get(pk=vendor_id)
        performance = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        context['vendor'] = vendor
        context['performance'] = performance
        return context
