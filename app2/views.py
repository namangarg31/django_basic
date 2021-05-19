from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth   #importing the User and auth
# Create your views here.
def compute(request):
    if request.method=='POST':
        var1 = request.POST['my_user']
        var2 = request.POST['f_name']
        var3 = request.POST['l_name']
        var4 = request.POST['e_mail']
        var5 = request.POST['my_password']
        my_obj = User.objects.create_user(username = var1,first_name = var2,last_name = var3,email = var4,password = var5)
        my_obj.save()
        print("User created successfully")
        return redirect('/')
    else :
        return render(request,'login_page.html')

