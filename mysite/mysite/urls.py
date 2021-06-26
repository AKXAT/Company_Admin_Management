"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from mysite.empman.views import editCompany
from django.contrib import admin
from django.urls import path
from empman import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.companyShowView,name='index'),
    path('delete/<int:id>',views.deleteCompany,name='deletecomp'),
    path('<int:id>/edit',views.editCompany,name='editcomp'),
    path('<int:id>/employee/',views.viewEmployee,name='showemp')
]
