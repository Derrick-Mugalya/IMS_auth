from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models
from .models import CustomerStock
from rest_framework import fields, serializers

# insert data  into the database

class CustomerStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerStock
        fields = '__all__'

# Fetch data from the database

