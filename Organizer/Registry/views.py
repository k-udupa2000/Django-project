from django.shortcuts import render, HttpResponse

from .forms import LoginForm, RegistrationForm
def home(request):
    #return HttpResponse('Login page')
    return render(request, 'Registry/home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            HttpResponse("Successful")

    return render(request, '/login.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register/app')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'Registry/signup.html', args)
