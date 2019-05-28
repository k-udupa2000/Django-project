from django.shortcuts import render, HttpResponse

def home(request):
    #return HttpResponse('Login page')
    return render(request, reverse_lazy('Registry/login.html'))