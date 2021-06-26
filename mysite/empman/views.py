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
            return HttpResponsePermanentRedirect('/')
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