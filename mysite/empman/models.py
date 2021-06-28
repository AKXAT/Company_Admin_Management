from datetime import date, datetime #so we can autofill the current date
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
# Create your models here.

class companyModel(models.Model): #this is the company model 
    company_name = models.CharField(max_length=100,blank=False)
    company_created = models.DateField(blank=False)

class employeeModel(models.Model): #Employee models for each company hence we make use of foreign key
    employee_company_name = models.ForeignKey(companyModel,on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100,blank=False)
    employee_created = models.DateField(blank=False)
