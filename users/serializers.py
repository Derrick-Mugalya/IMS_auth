from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models
from .models import Register
from rest_framework import fields, serializers
from django.contrib.auth import authenticate
     

# register serializer
class RegisterSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Register
        # fields = '__all__'
        fields = ('address', 'phone', 'register_as', 'hasAgreed')       
       
# user serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    register = RegisterSerializer(required=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password', 'register')
        extra_kwargs = {'password': {'write_only':True},
        }

    def create(self, validated_data):
        register_data = validated_data.pop('register')
        password = validated_data.get('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Register.objects.create(user=user, **register_data)
        return user



#login serializer

class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        else:
            raise serializers.ValidationError('Email/Password combination is incorrect, please try logging in again')


#password change

class ChangePasswordSerializer(serializers.Serializer):

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

#password reset



