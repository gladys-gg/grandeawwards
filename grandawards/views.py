from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm,NewProjectForm
from .models import *

# Create your views here.
def index(request):
    projects=Project.objects.all()
    return render(request,'index.html',{'projects':projects})

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # Profile.get_or_create(user=request.user)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Account created for { username }!!')
            return redirect('index')

    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'sign-up.html', context)

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            messages.success(request,('You information is not valid'))
            return redirect('sign-in')

    else:
        return render(request,'sign-in.html')

def signout(request):  
    logout(request) 

    return redirect('sign-in')
