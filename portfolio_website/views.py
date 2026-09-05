from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required , permission_required 
from .models import skill , projects , contact , experience
from .form import LoginForm

def log_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request , 'log_in.html' , {'form': form})

def home(request):
    return render(request , 'home.html')
def contact_view(request):
    return render(request , 'contact.html')
def tester(request):
    return render(request , 'tester.html')


# Create your views here.
