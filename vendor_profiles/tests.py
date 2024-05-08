from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vendor, HistoricalPerformance
from .serializers import VendorSerializer, HistoricalPerformanceSerializer
from purchase_orders.models import PurchaseOrder

# Test cases for Vendor model
class VendorTests(APITestCase):
    # Set up test data
    def setUp(self):
        # Create a vendor instance
        self.vendor = Vendor.objects.create(
            name="testvendor",
            contact_details="testcontactdetails",
            address="testaddress",
            vendor_code="testvendorcode",
        )
        # Create a historical performance instance
        self.historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.5,
            quality_rating_avg=3.5,
            average_response_time=2.5,
            fulfillment_rate=0.5,
        )

    # Test getting a vendor
    def test_get_vendor(self):
        url = reverse("vendor_retrieve_update_destroy", args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "testvendor")

    # Test getting historical performance
    def test_get_historical_performance(self):
        url = reverse("historical_performance", args=[self.historical_performance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["metrics"]["vendor"], self.vendor.id)
