from django.shortcuts import render

# Create your views here.
def setCookies(request):
    response= render(request, 'set_cookies.html')
    response.set_cookie('token',"tk121")
    return response


def GetCookies(request):
    id=request.COOKIES.get('token')
    return render(request, 'get_cookies.html' ,{'id':id})


def DelCookies(request):
    response= render(request, 'del_cookies.html')
    response.delete_cookie('token')
    return response