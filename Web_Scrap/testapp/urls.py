from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('hello/', views.hello),
    path('fuckoff/', views.fuckoff)
]