from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, loginSerializer

from rest_framework import status
from django.contrib.auth.models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated
from .serializers import ChangePasswordSerializer
from rest_framework.views import APIView


class RegisterAPI(generics.GenericAPIView):  
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):  

        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({                                  
        'user': UserSerializer(user, 
        context=self.get_serializer_context()).data,  
        'token': AuthToken.objects.create(user)[1] 
        })



#loginAPI
class loginAPI(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request, *args, **kwargs):   
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)    
        user = serializer.validated_data

        return Response({                                  
        'user': UserSerializer(user, 
        context=self.get_serializer_context()).data,     
        'token': AuthToken.objects.create(user)[1]
          
        })

#Get_User API

class UserAPI(generics.RetrieveAPIView):  
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer 

    def get_object(self):
        return self.request.user


#password change api

class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response("Success.", status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#password reset

# class PasswordResetView(generics.GenericAPIView):
    
#     serializer_class = PasswordResetSerializer
#     model = User


