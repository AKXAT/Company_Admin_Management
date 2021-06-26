from datetime import date, datetime
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
# Create your models here.

class companyModel(models.Model):
    company_name = models.CharField(max_length=100,blank=False)
    company_created = models.DateField(default=datetime.now,blank=False)

class employeeModel(models.Model):
    employee_company_name = models.ForeignKey(companyModel,on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100,blank=False)
    employee_created = models.DateField(default=datetime.now,blank=False)
