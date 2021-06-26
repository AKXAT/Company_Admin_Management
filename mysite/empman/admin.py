from django.contrib import admin
from empman.models import companyModel,employeeModel
# Register your models here.
admin.site.register(companyModel)
admin.site.register(employeeModel)