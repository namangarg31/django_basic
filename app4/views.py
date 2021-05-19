from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth   #importing the User and auth
# Create your views here.
def compute(request):  # logout function
    auth.logout(request)
    return redirect('/')
