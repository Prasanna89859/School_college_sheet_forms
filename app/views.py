from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def School_sheets(request):
    ESFO=SchoolForms()
    d={'ESFO':ESFO}
    if request.method =='POST':
        FSCO=SchoolForms(request.POST)
        if FSCO.is_valid():
            FSCO.save()
            return HttpResponse('Form school completed  sucssfully......')
        else:
            return HttpResponse('invalid School sheet.....')
    return render(request,'School_sheets.html',d)


def College_sheets(request):
    CFSP=collegeForms()
    d={'CFSP':CFSP}
    if request.method == 'POST':
        FCFS=collegeForms(request.POST)
        if FCFS.is_valid():
            FCFS.save()
            return HttpResponse('form college form sheet completed.....')
        else:
            return HttpResponse('invalid collge sheet.....')
    return render(request,'College_sheets.html',d)

