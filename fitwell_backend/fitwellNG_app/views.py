from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'frontend/index.html')

def sign_up(request):
    form = CustomUserCreationForm()
    if (request.method == "POST"):
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        return render(request, 'registration/sign-up.html', {'form': form})
    return render(request, 'registration/sign-up.html', {'form': form})  

def login(request):
    if(request.method == 'POST'):
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')