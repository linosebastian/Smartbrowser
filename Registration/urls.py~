"""Registraion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from Registrationapp.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
     url(r'^$',main),
     url(r'^reg',registration,name='reg'),
     url(r'^home',home,name='home'),
     url(r'^log',login,name='log'),
     url(r'^gohome',gohome,name='gohome'),
     url(r'^download',download,name='download'),
     url(r'^data',data,name='data'),

]
