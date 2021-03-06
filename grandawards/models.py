from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    profile_pic= CloudinaryField('image')
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100,blank=True)
    bio= models.TextField()
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)    

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.fullname
    
class Project(models.Model):
    title= models.CharField(max_length=100)
    project_image= CloudinaryField('image')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    description= models.TextField()
    link= models.CharField(max_length=250)

    def __str__(self):
        return self.title + '' + self.description
    
    def save_project(self):
        self.save()


    @classmethod
    def search_by_title(cls,search_term):
        '''
        method to search projects based on name
        '''
        
        title = cls.objects.filter(title__icontains=search_term).all()
        return title