"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views   # from firsapp we are importing views app
from app2 import views as views2
from app3 import views as views3
from app4 import views as views4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1),  # if the path is blank then it means localhost:8000 it should be handled by views.fun1
    path('fun2/',views.fun2),
    path('button/',views.fun3),
    path('outputExpression/',views.compute),
    path('signup/',views2.compute),
    path('login/',views3.compute),
    path('logout/',views4.compute),
]
