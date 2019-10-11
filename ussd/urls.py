from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import url
from .views import IMSUSSDAPIView


urlpatterns = [
    path('api/imsussd/', IMSUSSDAPIView.as_view(), name='ims-callback'),
    ]