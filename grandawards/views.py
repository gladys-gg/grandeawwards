from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UserRegisterForm
from django.urls import reverse, resolve
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import ProfileForm,NewProjectForm
from .models import *
from django.contrib import messages
from .serializers import ProfileSerializer,ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    projects=Project.objects.all()
    return render(request,'index.html',{'projects':projects})

@login_required
def UserProfile(request, username):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    projects = Project.objects.filter(profile=profile)
    if url_name == 'profile':
        projects = Project.objects.filter(profile=profile)
    else:
        projects = profile.favourite.all()
    
    # Profile Stats
    projects_count = Project.objects.filter(profile=profile).count()

    context = {
        'projects': projects,
        'profile':profile,
        'projects_count':projects_count,

    }
    return render(request, 'profile.html', context)


@login_required
def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user_id=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            profile.fullname = form.cleaned_data.get('fullname')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile', profile.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {
        'form':form,
    }
    return render(request, 'editprofile.html', context)


#an api to handle the profile requests
@api_view(['GET','POST'])
def profile_list(request, format=None):
    #get all profiles
    if request.method =='GET':
        profiles = Profile.objects.all()
        #serialize them
        serializer = ProfileSerializer(profiles, many=True)
        #return json
        return Response(serializer.data)
    if request.method =='POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def profile_detail(request,id, format=None):
    try:
        Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#an api to handle the project requests
@api_view(['GET','POST'])
def project_list(request, format=None):
    #get all profiles
    if request.method =='GET':
        projects = Project.objects.all()
        #serialize them
        serializer = ProjectSerializer(projects, many=True)
        #return json
        return Response(serializer.data)
    if request.method =='POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def project_detail(request,id, format=None):
    try:
        Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@login_required   
def NewProject(request):
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form=NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.user=request.user.profile
            data.save()
            return redirect('index')
        else:
            form=NewProjectForm()

    return render(request, 'newproject.html',{'form':NewProjectForm})

def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term).all()
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any projects yet"
    return render(request, 'search.html', {'message': message})
        
        
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
    return render(request, 'registration/sign-up.html', context)


def signout(request):  
    logout(request) 

    return redirect('index')
