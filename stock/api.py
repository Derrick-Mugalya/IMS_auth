from rest_framework import viewsets, permissions
from .serializers import CustomerStockSerializer
from .models import CustomerStock
from django.contrib.auth.models import User

from stock.models import CustomerStock

class CustomerStockViewSet(viewsets.ModelViewSet):
    # queryset = CustomerStock.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    serializer_class=CustomerStockSerializer

    def get_queryset(self):
        return self.request.user.CustomerStock.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

