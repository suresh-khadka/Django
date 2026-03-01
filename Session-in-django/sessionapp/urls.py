from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('set/' , views.Set),
    path('get/' , views.Get),
    path('del/' , views.Del),
]