from django.shortcuts import render
from django.http import HttpResponse  # helps in sending the http request 
# Create your views here.
def fun1(request):
    return render(request,"home.html")
def fun2(request):
    return HttpResponse("<h1>This is heading 1</h1>")
def fun3(request):
    return render(request,'file2.html')  
def compute(request):
    x = int(request.POST['val_1'])  # GET is not secure so use POST
    y = int(request.POST['val_2'])
    symbol = request.POST['val_exp']
    result = 0
    if symbol=='+':
        result = x+y
    elif symbol=='-':
        result = x-y
    elif symbol == '*':
        result = x*y
    elif symbol == '/':
        result = x/y                
    return render(request,'outputExpression.html',{'final_val':result})          