from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('setCookies/', views.setCookies),
    path('getCookies/', views.GetCookies),
    path('delCookies/', views.DelCookies),
]