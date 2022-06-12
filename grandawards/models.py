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
