from django.contrib import admin
from django.urls import path,include

from gemapp import views

urlpatterns = [
    path('',views.enquiry),
    path('admission/',views.admission),
    path('login/', views.login),
       ]