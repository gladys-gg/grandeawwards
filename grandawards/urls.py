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
    path('profiles/',views.profile_list),
    path('profiles/<int:id>', views.profile_detail),
        # Profile Section
    path('profile/<int:user_id>', views.UserProfile, name='profile'),
    path('profile/edit', views.EditProfile, name="editprofile"),
    # User Authentication

    path('sign-up/',views.register,name='sign-up'),
    path('accounts/sign-in/',views.signin,name='sign-in'),
    path('sign-out/', views.signout, name='sign-out'),
    
    #project
    path('newproject', views.NewProject, name='newproject'),
        #profile paths
    path('projects/',views.project_list),
    path('projects/<int:id>', views.project_detail),
    

]

urlpatterns=format_suffix_patterns(urlpatterns)
