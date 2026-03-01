from django.shortcuts import render

# Create your views here.

def Set(request):
    request.session['fname']='suresh'
    request.session['lname']='khadka'
    return render(request , 'set.html')

def Get(request):
    # f_name=request.session['fname']
    f_name=request.session.get('fname')
    l_name=request.session.get('lname')
    return render(request , 'get.html' ,{
        "fname":f_name,
        'lname':l_name,
    })

def Del(request):
    if 'lname' in request.session:
        del request.session['lname']

    return render(request , 'delete.html')