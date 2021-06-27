from django import forms
from django.shortcuts import render,HttpResponsePermanentRedirect
from empman.forms import companyForm,employeeForm
from empman.models import companyModel,employeeModel
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