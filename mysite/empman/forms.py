from django import forms
from django.forms import widgets
from empman.models import companyModel,employeeModel

class companyForm(forms.ModelForm):
    class Meta:
        model = companyModel
        fields = ['company_name','company_created']
        widgets = {
            'company_name' : forms.TextInput(attrs={'class':'form-control '}),
            'company_created':forms.TextInput(attrs={'class':'form-control'})
        }

class employeeForm(forms.ModelForm):    
    class Meta:
        model = employeeModel
        fields = ['employee_company_name','employee_name','employee_created'] 
        
        widgets = {
            'employee_company_name' : forms.TextInput(attrs={'class':'form-control '}),
            'employee_company_name': forms.HiddenInput,
            'employee_name':forms.TextInput(attrs={'class':'form-control'}),
            'employee_created':forms.TextInput(attrs={'class':'form-control'})
        }  


        