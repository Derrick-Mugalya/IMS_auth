from django.db import models

# Create your models here.


class IMSUSSD(models.Model):
    sessionId = models.CharField(max_length=100)    #A unique value generated when the session starts and sent every time a mobile subscriber response has been received
    phoneNumber = models.CharField(max_length=100)  #The number of the mobile subscriber interacting with your ussd application
    networkCode = models.CharField(max_length=100)  #The telco of the phoneNumber interacting with your ussd application.
    serviceCode = models.CharField(max_length=100)  #This is your USSD code. Please note that it doesn’t show your channel on shared USSD codes.
    text = models.CharField(max_length=100)         #This shows the user input. It is an empty string in the first notification of a session. After that, it concatenates all the user input within the session with a * until the session ends.

    def __str__(self):
        return f'{self} IMSUSSD'