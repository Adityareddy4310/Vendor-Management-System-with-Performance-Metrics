from django.urls import path
from .api_views import VendorPerformanceEvaluationAPIView


from .api_views import (
    VendorListCreateAPIView,
    VendorRetrieveUpdateDestroyAPIView,
    VendorPerformanceEvaluationAPIView,  # Corrected import
)

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('<int:id>/performance/', VendorPerformanceEvaluationAPIView.as_view(), name='vendor-performance-evaluation'),

]
