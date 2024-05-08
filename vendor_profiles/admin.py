from django.contrib import admin
from .models import Vendor, HistoricalPerformance

# Admin class for Vendor model
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('name', 'address', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ('name', 'address', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')

# Admin class for HistoricalPerformance model
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('vendor', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ('vendor', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')

# Register models with custom admin classes
admin.site.register(Vendor, VendorAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
