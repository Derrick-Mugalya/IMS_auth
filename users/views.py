from django.shortcuts import render

# Create your views here.

def passwordconfirm(request):
    return render(request, 'users/password.html')