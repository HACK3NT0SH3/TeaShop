from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import signupform
from django.http import HttpResponse

def home(request):
    return render(request, 'pirip/index.html')

def about(request):
    return render(request, 'pirip/about_us.html')

def delivery(request):
    return render(request, 'pirip/delivery.html')

def payment(request):
    return render(request, 'pirip/payment.html')

def catalog(request):
    return render(request, 'pirip/catalog.html')

def cart(request):
    return render(request, 'pirip/cart.html')

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Next')
    else:
        return render(request, 'pirip/login.html')

def signupview(request):
    if request.method=="POST":
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signupform()
    return render(request, 'pirip/signup.html', {'form':form})

def item(request):
    return render(request, 'pirip/item.html')

def Next(request):
    return render(request, 'pirip/profile.html')
