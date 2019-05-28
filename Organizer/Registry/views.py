from django.shortcuts import render, HttpResponse

def home(request):
    #return HttpResponse('Login page')
    return render(request, 'Registry/login.html')
