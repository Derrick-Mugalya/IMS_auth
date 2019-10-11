from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='IMS API')

urlpatterns = [
    path('api_documentation/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('stock.urls')),
    path('', include('ussd.urls')),
    url(r'^swagger/', schema_view),
    ]
