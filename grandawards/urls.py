from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.index, name='index'),
    #profile paths
    path('profiles/',views.profile_list, name='profiles_api'),
    path('profiles/<int:id>', views.profile_detail),
        # Profile Section
    path('profile/edit', views.EditProfile, name="editprofile"),
    path('search/', views.search_results, name='search'),

    
    #project
    path('newproject', views.NewProject, name='newproject'),
        #profile paths
    path('projects/',views.project_list, name='projects_api'),
    path('projects/<int:id>', views.project_detail),
    

]

urlpatterns=format_suffix_patterns(urlpatterns)
