from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.generic import View
from django.http import JsonResponse
from time import time
from .SentimentAnalysis import analize
from .TextSummarize import generate_summary
from json import dumps

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

def textSumm(request):
    if request.method=='POST':
        upFile=request.FILES['text'].read()
        upFile=str(upFile,'utf-8')
        upFile=generate_summary(upFile,5)
        res={'ST':upFile}
        dJSON=dumps(res)
        return render(request,'Assistant/text_Summ.html',{'data':dJSON})
    return render(request,'Assistant/text_Summ.html')

class AjaxHandler(View):
    def get(self,request):
        text=request.GET.get('product_url')
        data=analize(text)
        if request.is_ajax():
            return JsonResponse(data,status=200)
        return render(request,'Assistant/sentiment.html')