from django.contrib import admin
from .models import PurchaseOrder

# Define admin class for PurchaseOrder model
class PurchaseOrderAdmin(admin.ModelAdmin):
    # Define fields to display in the admin list view
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date')
    # Define filters for the admin list view
    list_filter = ('status', 'vendor', 'order_date', 'delivery_date')
    # Define fields to search in the admin list view
    search_fields = ('po_number', 'vendor', 'order_date', 'delivery_date', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date')

# Register PurchaseOrder model with the custom admin class
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
