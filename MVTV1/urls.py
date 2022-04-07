
from django.contrib import admin
from django.urls import path 
from MVTV1.views import home_page, family_members

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/', home_page),
    path('family_members', family_members),

]
