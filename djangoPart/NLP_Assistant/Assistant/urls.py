from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='homepage'),
    path('results/',views.runScript,name='script'),
]