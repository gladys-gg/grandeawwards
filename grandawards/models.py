from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    profile_pic= CloudinaryField('image')
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100,blank=True)
    bio= models.TextField()

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    project_image= CloudinaryField('image')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=100)
    description= models.TextField()
    link= models.CharField(max_length=250)


    def save_project(self):
        self.save()


    @classmethod
    def search_by_name(cls,search_term):
        '''
        method to search projects based on name
        '''
        projects=cls.objects.filter(name__icontains=search_term)

        return projects
