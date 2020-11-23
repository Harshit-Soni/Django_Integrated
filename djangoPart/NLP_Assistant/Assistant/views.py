from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.generic import View
from django.http import JsonResponse
from time import time
from .SentimentAnalysis import analize


def HomePage(request):
    return render(request, 'Assistant/index.html')

def runScript(request):
    print('start')
    from . import script
    return render(request,'Assistant/index.html')

def chatbotpage(request):
    return render(request,'Assistant/chatbotQA.html')

def requestQuerry(request):
    render(request,'Assistant/chatbotQA.html')

def sentimentAnalysis(request):
    return render(request,'Assistant/sentiment.html')

class AjaxHandler(View):
    def get(self,request):
        text=request.GET.get('product_url')
        data=analize(text)
        if request.is_ajax():
            return JsonResponse(data,status=200)
        return render(request,'Assistant/sentiment.html')