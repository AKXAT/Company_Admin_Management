from django import forms #import the forms so we make use of model forms
from django.forms import widgets #we will be using the widgets options to manipulate the form
from empman.models import companyModel,employeeModel #import the models that we have created

class companyForm(forms.ModelForm):
    class Meta:
        model = companyModel
        fields = ['company_name','company_created'] #getting the fileds from the company model
        widgets = {
            'company_name' : forms.TextInput(attrs={'class':'form-control '}), #bootstrap class
            'company_created':forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}) #bootstrap class
        }

class employeeForm(forms.ModelForm):    
    class Meta:
        model = employeeModel
        fields = ['employee_company_name','employee_name','employee_created'] #getting the fileds from the employee model
        
        widgets = {
            'employee_company_name' : forms.TextInput(attrs={'class':'form-control '}),#bootstrap class
            'employee_company_name': forms.HiddenInput, #so the user is not able to edit the company model linked to that emplopyee
            'employee_name':forms.TextInput(attrs={'class':'form-control'}),#bootstrap class
            'employee_created':forms.TextInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'})#bootstrap class
        }  


        