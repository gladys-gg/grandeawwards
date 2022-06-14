from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from .models import Profile,Project

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ProfileForm(ModelForm):
    profile_pic= forms.ImageField(required=True)
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Full Name'}), required=True)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}), required=True)
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Website'}), required=True)

    class Meta:
        model = Profile
        fields = ['profile_pic', 'fullname', 'bio', 'url', 'location']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'url': forms.TextInput(attrs={'class':'form-control'}),
        }
