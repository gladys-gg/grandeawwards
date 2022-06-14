from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='gladys')
        self.profile = Profile.objects.create(user = self.user,bio = 'A self made developer',location= 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

class ProjectTest(TestCase):
    
    def test_search_by_title(self):
        self.profile.save()
        title = Project.search_by_title('akan')
        self.assertTrue(len(project) > 0)
        
    def test_save_project(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

