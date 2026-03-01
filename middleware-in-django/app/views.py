from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def middlewareView(request):
    print("this is a view")
    return HttpResponse("Your views")