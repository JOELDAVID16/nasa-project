from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.


def auth_login(request):
    if request.method=="POST":
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            return render(request,'home.html')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})    



def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')
def beginner(request):
    return render(request,'beginner.html')

def intermediate(request):
    return render(request,'intermediate.html')
def advance(request):
    return render(request,'advance.html')