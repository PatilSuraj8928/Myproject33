from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.
def insertopic_modelform(request):
    TMFO=Topic_modelform()
    d={'form':TMFO}

    if request.method=='POST':
        FD=Topic_modelform(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('<h1> Topic Inserted!!!<h1>')
    return render(request, 'Topic_modelform.html',d)


def insert_webpage(request):
    WMFO=Webpage_modelform()
    d1={'form':WMFO}

    if request.method=='POST':
        fd=Webpage_modelform(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('<center><h1>Webpage Inserted!!!</h1></center>')
    return render(request, 'insert_webpage.html',d1)

def insert_Access(request):
    AMFO=Access_modelform()
    d2={'form':AMFO}

    if request.method=='POST':
        data=Access_modelform(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('<center><h1>Access records inserted</h1></center>')

    return render(request, 'insert_Access.html',d2)