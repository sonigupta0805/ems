
from django.contrib import admin
from django.urls import path, include

from employee.views import (  user_login, user_logout,
    success, ProfileUpdate, MyProfile)

urlpatterns = [
  #  path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('poll/', include('poll.urls')),
    
    path('employee/', include('employee.urls')),

    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    
    path('profile/', MyProfile.as_view(), name="my_profile"),
    path('profile/update', ProfileUpdate.as_view(), name="update_profile"),
] 