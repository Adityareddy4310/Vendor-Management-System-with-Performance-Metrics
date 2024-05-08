from django.db import models
from vendor_profiles.models import Vendor
from django.db.models import signals
from vendor_profiles.models import Vendor, HistoricalPerformance
from django.db.models import Avg
from django.utils.timezone import now

# Define choices for status field
STATUS = (
    ("pending", "pending"),
    ("completed", "completed"),
    ("canceled", "canceled"),
)

# Define PurchaseOrder model
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=10)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=now)
    delivery_date = models.DateTimeField()
    items = models.JSONField(default=dict)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

# Define signal handler for post_save event
def historical_performance_handler(sender, instance, **kwargs):
    # Signal handling logic here

# Connect signal handler to post_save event of PurchaseOrder model
 signals.post_save.connect(historical_performance_handler, sender=PurchaseOrder)
