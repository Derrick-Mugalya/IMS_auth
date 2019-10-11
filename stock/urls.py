from rest_framework import routers
from .api import CustomerStockViewSet
from users.api import RegisterAPI

router = routers.DefaultRouter()
router.register('api/CustomerStock', CustomerStockViewSet, 'CustomerStock'),

urlpatterns = router.urls