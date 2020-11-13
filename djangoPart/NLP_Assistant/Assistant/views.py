from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
import time

def HomePage(request):
    return render(request, 'Assistant/index.html')

def runScript(request):
    print('start')
    from . import script
    print(123)
    return render(request,'Assistant/index.html')

def chatbotpage(request):
    return render(request,'Assistant/chatbotQA.html')

def requestQuerry(request):
    render(None,'Assistant/chatbotQA.html')