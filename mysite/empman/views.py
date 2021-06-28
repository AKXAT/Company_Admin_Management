from django import forms
from django.shortcuts import render,HttpResponsePermanentRedirect,HttpResponse
from empman.forms import companyForm,employeeForm
from empman.models import companyModel,employeeModel
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
import os

# Create your views here.


'''
The Below function is responsible for the Company Home Page View 
1. It contains a form to add new company which has a button to submit it 
2. It displays the added company just below the list 
'''
def companyShowView(request):
    if request.method == 'POST':
        form = companyForm(request.POST)
        if form.is_valid():
            form.save()
            form = companyForm() #to refresh and show blank form after the sumbit 
    else:
        form = companyForm()
    
    comp = companyModel.objects.all()
    return render(request,'empman/companyshow.html',{'form':form,'comp':comp})




'''
The below funtion is responsible for edit teh company details when the button is hit
'''

def editCompany(request,id):
    if request.method == 'POST':
        uniqueid = companyModel.objects.get(pk=id) #it gets the unique id of each company so its auto filled 
        requestpost = companyForm(request.POST,instance=uniqueid)
        if requestpost.is_valid():
            requestpost.save()
            return HttpResponsePermanentRedirect('/') #throws back to the home page
    else:
        uniqueid = companyModel.objects.get(pk=id)
        requestpost = companyForm(instance=uniqueid)
    return render(request,'empman/companyupdate.html',{'form':requestpost})




'''
The below funtion is responsible for deleteing the company from the comnpany model
'''

def deleteCompany(request,id):
    if request.method == 'POST':
        dele=companyModel.objects.get(pk=id) #to get unique id of the selected company model
        dele.delete()
        return HttpResponsePermanentRedirect('/')

#for testing 
# def viewEmployee(request,id):
#     print(id)
#     return render(request,'empman/employeeshow.html')





'''
the below funtion is responsible for viewing the Employee list view the company model is selected
1. It servers the option to add a new employee to the selected company model
2. Shows the list of employee for the specific compnay model
'''

def viewEmployee(request,id):
    initial = {'employee_company_name': id} # this is hidded in the form , usecase fo this is to add employee to their specific company model( which is represented by id)
    if request.method == 'POST':
        fm = employeeForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = employeeForm(initial=initial)
    company = companyModel.objects.get(id=id)
    employees = company.employeemodel_set.all() #employess of that company
    return render(request,'empman/employeeshow.html', {'fm':fm,'company':company, 'showemps':employees})





'''
The below funtion is responsible for deleteing the employee for the comnpany model
'''

def deleteEmployee(request,id):
    if request.method == 'POST':
        dele=employeeModel.objects.get(pk=id)
        dele.delete()
        return HttpResponsePermanentRedirect('/')





'''
The Below funtions is responsible for opening edit options for Employee Details
1. When the button is pressed it should open up a page that give the edit page 
'''

def editEmployee(request,id):
    if request.method == 'POST':
        uniqueid = employeeModel.objects.get(pk=id)
        requestpost = employeeForm(request.POST,instance=uniqueid)
        if requestpost.is_valid():
            requestpost.save()
            return HttpResponsePermanentRedirect('/')
    else:
        uniqueid = employeeModel.objects.get(pk=id)
        requestpost = employeeForm(instance=uniqueid)
    return render(request,'empman/employeeupdate.html',{'eform':requestpost})






'''
The below function is responsible for generating PDF - Please read docs at  https://xhtml2pdf.readthedocs.io/en/latest/usage.html#using-xhtml2pdf-in-django
'''

def downloadPdf(request,pk):

        company = companyModel.objects.get(pk=pk)
        employees = company.employeemodel_set.all() #employess of that company
        template_path = 'empman/pdfreport.html'
        context = {'employees': employees}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context) 

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response