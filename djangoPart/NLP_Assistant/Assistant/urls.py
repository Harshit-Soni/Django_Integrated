from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='homepage'),
    path('results/',views.runScript,name='script'),
    path('chatbot/',views.chatbotpage,name='chatbotQA'),
    path('',views.requestQuerry,name='reqQuerry'),
    path('SentAjax',views.sentimentAnalysis,name='sentAnalys'),
    path('sentAjax',views.AjaxHandler.as_view(),name='sentAjax'),
]