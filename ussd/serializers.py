from rest_framework import serializers
from .models import IMSUSSD

class IMSUSSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMSUSSD
        fields = '__all__'