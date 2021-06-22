from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader




def page1(request):
    return render(request, 'page2.html')
   

def page2(request):
    return render(request, 'page3.html')
   



# Create your views here.
