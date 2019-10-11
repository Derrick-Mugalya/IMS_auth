from django.shortcuts import render

#this is where the views are done

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .serializers import IMSUSSDSerializer
from .models import IMSUSSD
from rest_framework.permissions import AllowAny
# from rest_framework.permissions import IsAdminUser


class IMSUSSDAPIView(generics.ListCreateAPIView):
    queryset = IMSUSSD.objects.all()
    serializer_class = IMSUSSDSerializer
    permission_classes = [AllowAny]


    # def create(self, request):
    #     print (request.data, "this is request.data")


