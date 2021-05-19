from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth   #importing the User and auth
# Create your views here.
def compute(request):
    if request.method=='POST':
        entered_username = request.POST['user_name']
        entered_password = request.POST['pass_word']
        x = auth.authenticate(username=entered_username,password=entered_password)
        if x is None:
            return redirect('/login/')
        else :
            print("Yes the user exist")
            auth.login(request,x)  # user will be authenticated by using this statement
            return redirect('/')
    else :
        return render(request,'login.html')            