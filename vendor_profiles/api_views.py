from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from vendor_profiles.models import Vendor, HistoricalPerformance
from vendor_profiles.serializers import VendorSerializer, HistoricalPerformanceSerializer
from purchase_orders.models import PurchaseOrder  # Import PurchaseOrder model if needed
from purchase_orders.serializers import PurchaseOrderSerializer  # Import PurchaseOrderSerializer


# Class definitions without the circular import

class PurchaseOrderListCreateAPIView(ListCreateAPIView):
    """
    API view for listing and creating purchase orders.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PurchaseOrderSerializer  # Use PurchaseOrderSerializer here
    queryset = PurchaseOrder.objects.all()  # If PurchaseOrder model is used, ensure it's imported correctly


class PurchaseOrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and destroying individual purchase orders.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    lookup_field = "id"


class VendorListCreateAPIView(ListCreateAPIView):
    """
    API view for listing and creating vendors.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and destroying individual vendors.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    lookup_field = "id"



class VendorPerformanceEvaluationAPIView(APIView):
    """
    API view for evaluating historical performance metrics of a vendor.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                description="Vendor ID",
                required=True,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
            )
        ],
        examples=[
            OpenApiExample(
                name="Vendor 1",
                value={
                    "id": 1,
                    "name": "Vendor 1",
                    "address": "123 Main St",
                    "city": "Austin",
                    "state": "TX",
                    "zip_code": "78701",
                    "country": "USA",
                    "phone_number": "512-555-5555",
                    "email": "vendor1@example.com",
                    "contact_name": "John Doe",
                    "on_time_delivery_rate": 0.85,
                    "quality_rating_avg": 0.92,
                    "average_response_time": 2.1,
                    "fulfillment_rate": 0.88,
                },
            ),
            OpenApiExample(
                name="Vendor 2",
                value={
                    "id": 2,
                    "name": "Vendor 2",
                    "address": "456 Oak St",
                    "city": "New York",
                    "state": "NY",
                    "zip_code": "10001",
                    "country": "USA",
                    "phone_number": "212-555-5555",
                    "email": "vendor2@example.com",
                    "contact_name": "Jane Doe",
                    "on_time_delivery_rate": 0.78,
                    "quality_rating_avg": 0.88,
                    "average_response_time": 3.5,
                    "fulfillment_rate": 0.82,
                },
            ),
        ],
    )
    def get(self, request, id, *args, **kwargs):
        metrics = HistoricalPerformance.objects.filter(vendor=id)
        metrics = HistoricalPerformanceSerializer(metrics, many=True).data

        return Response({'metrics': metrics})
