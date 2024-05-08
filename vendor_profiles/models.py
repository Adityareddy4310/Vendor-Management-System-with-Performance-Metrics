from django.db import models

# Define base metrics model
class BaseMetrics(models.Model):
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    class Meta:
        abstract = True

# Define Vendor model
class Vendor(BaseMetrics):
    name = models.CharField(max_length=50)
    contact_details = models.TextField(max_length=150)
    address = models.TextField(max_length=200)
    vendor_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# Define HistoricalPerformance model
class HistoricalPerformance(BaseMetrics):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor.name
