from django.shortcuts import render, redirect

def HomePage(request):
    return render(request, 'Assistant/index.html')
