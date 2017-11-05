"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	return render(request, "index.html")

def description(request):
    return render(request, "description.html")

def contact(request):
    return render(request, "contact.html")

def student_detail(request):
    return render(request, "student_detail.html")

def student_list(request):
    return render(request, "student_list.html")

urlpatterns = [
	url(r'^$', hello),
    url(r'^description/$', description),
    url(r'^contact/$', contact),
    url(r'^student_detail/$', student_detail),
    url(r'^student_list/$', student_list),
    url(r'^admin/', admin.site.urls),
]
