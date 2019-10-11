from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# Create your models here.

MY_CHOICES = (('F', 'Farmer'),
              ('I', 'Industry'),
              ('V/F', 'Vendor/Merchant'))
              

MY_CHOICES2 = ((1, 'Bakery and bread'),
               (2, 'Meat and sea food'),
               (3, 'Pasta and rice'),
               (4, 'Oils, sauces, salad dressings and condiments'),
               (5, 'cereals and breakfast foods'),
               (6, 'Soups and canned goods'),
               (7, 'Frozen foods'),
               (8, 'Dairy, chinese and eggs'),
               (9, 'Snacks and crackers'),
               (10, 'cereals and breakfast foods'),
               (11, 'Produce'),
               (12, 'Drinks'))



class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    register_as = models.CharField(max_length=20)
    hasAgreed = models.BooleanField(default=False)
    # register_as = models.TextChoices('vendor', 'industry', 'farmer')
      

    def __str__(self):
        return f'{self.user} Register'

