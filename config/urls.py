"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from config import views
#from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('profile', views.profile),
    path('getdemo1', views.getdemo),
    path('address/', include('address.urls')),
    path('myapp/', include('myapp.urls')),
    path('survey/', include('survey.urls')),
    path('fileup/', include('fileup.urls')),
    path('shop/', include('shop.urls')),
    path('oraform/', include('oraform.urls')),
    path('login/', include('login.urls')),
    path('myjson/', include('myjson.urls')),
]
