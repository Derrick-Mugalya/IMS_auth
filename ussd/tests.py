from django.test import TestCase

# Create your tests here.

# from django.shortcuts import render
# from stock.models import CustomerStock
# from django.contrib.auth.models import User
# from django.db import models

# Create your views here.

# let have where users can report produce.
# another one where users can report problems encountered with their products like pests or diseases attacking their crops.
# and lets give them an option to select from a list of options or type it in case its not in the options

# produce = input('Welcome to the IMS USSD system. Press 1 to report produce and 2 to report a problem: ')
# if produce == '1':
#     report = input('Which of the following would you like to execute.\n1. Add stock\n2. Reduce stock\n3. Other\n')
#     if report == '1':
#         #one should be able to add stock to the database using his account
#         #authentication
#         name = input('Enter your username')
#         password = input('Enter your password')
#         def validate(request):
#             return 'i am to complete this function'

#     elif report == '2':
#         #one has to be able to reduce the stock from the users account
#         print ('still working on this')
#     else:
#         response = input('Specify the problem that you are facing with your crops of any other that you would like us to know')
# else:
#     print ('We did not understand your input.')

# <?php
# // Reads the variables sent via POST from our gateway
# $sessionId   = $_POST["sessionId"];
# $serviceCode = $_POST["serviceCode"];
# $phoneNumber = $_POST["phoneNumber"];
# $text        = $_POST["text"];


# class Parameters(models.Model):
#     sessionId = models.CharField(max_length=100)    #A unique value generated when the session starts and sent every time a mobile subscriber response has been received
#     phoneNumber = models.CharField(max_length=100)  #The number of the mobile subscriber interacting with your ussd application
#     networkCode = models.CharField(max_length=100)  #The telco of the phoneNumber interacting with your ussd application.
#     serviceCode = models.CharField(max_length=100)  #This is your USSD code. Please note that it doesn’t show your channel on shared USSD codes.
#     Text = models.CharField(max_length=100)         #This shows the user input. It is an empty string in the first notification of a session. After that, it concatenates all the user input within the session with a * until the session ends.

#     def __str__(self):
#         return Parameters

# from twilio.rest import Client

# # Your Account SID from twilio.com/console
# account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# # Your Auth Token from twilio.com/console
# # auth_token  = "your_auth_token"

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+256755645169", 
#     from_="+15017250604",
#     body="Hello from Python!")

# print(message.sid)

# sessionId = ('')
# phoneNumber = ('')
# networkCode = ('')
# serviceCode = ('')
# text = ('')

# if text == "":
#     # This is the first request. Note how we start the response with CON
#     text = input('CON Welcome to the IMS USSD system.\n Press 1 to report produce and 2 to report a problem: \n')
    
#     if text == "1":
#     #Business logic for first level response
#         alter_stock = input('Which of the following would you like to execute.\n1. Add stock\n2. Reduce stock\n3. Other: \n')
#         if alter_stock == '1':
#             add_stock = input('Enter the amount of stock and the quantity you would like to add:\n ')
#         elif text == '1':
#             reduce_stock =input('Enter the name and amount of stock you would like to reduce:\n ')
#         else:
#             print('sorry we did not understand your input')

#     elif text == '2':
#         problem = input('Write the detailed name of the problem that you would want to report:\n ')
#         if problem != 0:
#             print('Thank you for using the IMS system, you will be contacted shortly')
#         else:
#             print ('sorry, the field cannot be left empty')

#     else:
#         text = input('Sorry, we did no understand your input')

# } else if ($text == "2") {
#     // Business logic for first level response
#     // This is a terminal request. Note how we start the response with END
#     $response = "END Your phone number is ".$phoneNumber;

# } else if($text == "1*1") { 
#     // This is a second level response where the user selected 1 in the first instance
#     $accountNumber  = "ACC1001";

#     // This is a terminal request. Note how we start the response with END
#     $response = "END Your account number is ".$accountNumber;

# } else if ( $text == "1*2" ) {
#     // This is a second level response where the user selected 1 in the first instance
#     $balance  = "KES 10,000";

#     // This is a terminal request. Note how we start the response with END
#     $response = "END Your balance is ".$balance;
# }

# // Echo the response back to the API
# header('Content-type: text/plain');
# echo $response;