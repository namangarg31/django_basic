from django.contrib import admin
from .models import employee   # we have to import our table employee from models
# Register your models here.
admin.site.register(employee)  # to register the employee table