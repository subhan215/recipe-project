"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('' , home , name = "home") ,
    path('contact/' , contact , name = "contact") ,
    path('recipes/' , recipes , name = "recipes") ,
    path('about/' , about , name = "about") ,
    path('success_page/' , success_page  , name = "success_page") , 
    path('admin/', admin.site.urls),
    path('delRecipe/<id>/'  ,delRecipe , name = "delRecipe") , 
    path('updRecipe/<id>/'  ,updRecipe , name = "updRecipe") , 
    path('login/'  ,logInPage , name = "login")  , 
    path('register/'  ,register , name = "register")  , 
    path('logout/'  ,logOutPage , name = "logout") , 
    path('allRecipes/' ,allRecipes , name = "allRecipes" )
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
  
