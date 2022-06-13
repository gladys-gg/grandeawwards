from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('fullname','bio','profile_pic','location','user','url')
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('title','project_image','profile','description','link')
