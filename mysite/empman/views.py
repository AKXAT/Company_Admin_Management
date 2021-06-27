from django import forms
from django.shortcuts import render,HttpResponsePermanentRedirect,HttpResponse
from empman.forms import companyForm,employeeForm
from empman.models import companyModel,employeeModel
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
import os

# Create your views here.
def companyShowView(request):
    if request.method == 'POST':
        form = companyForm(request.POST)
        if form.is_valid():
            form.save()
            form = companyForm()
    else:
        form = companyForm()
    
    comp = companyModel.objects.all()
    return render(request,'empman/companyshow.html',{'form':form,'comp':comp})

def editCompany(request,id):
    if request.method == 'POST':
        uniqueid = companyModel.objects.get(pk=id)
        requestpost = companyForm(request.POST,instance=uniqueid)
        if requestpost.is_valid():
            requestpost.save()
            return HttpResponsePermanentRedirect('/')
    else:
        uniqueid = companyModel.objects.get(pk=id)
        requestpost = companyForm(instance=uniqueid)
    return render(request,'empman/companyupdate.html',{'form':requestpost})

def deleteCompany(request,id):
    if request.method == 'POST':
        dele=companyModel.objects.get(pk=id)
        dele.delete()
        return HttpResponsePermanentRedirect('/')


# def viewEmployee(request,id):
#     print(id)
#     return render(request,'empman/employeeshow.html')

def viewEmployee(request,id):
    initial = {'employee_company_name': id}
    if request.method == 'POST':
        fm = employeeForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = employeeForm(initial=initial)
    company = companyModel.objects.get(id=id)
    employees = company.employeemodel_set.all() #employess of that company
    return render(request,'empman/employeeshow.html', {'fm':fm,'company':company, 'showemps':employees})


def deleteEmployee(request,id):
    if request.method == 'POST':
        dele=employeeModel.objects.get(pk=id)
        dele.delete()
        return HttpResponsePermanentRedirect('/')

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