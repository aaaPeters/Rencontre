"""Rencontre URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from User import views as User_views

urlpatterns = [
    url(r'^user/register/$', User_views.register, name = 'userRegister'),
    url(r'^user/verification/$', User_views.verification, name = "userVerification"),
    url(r'^user/resetPassword/$', User_views.resetPassword, name = 'resetPassword'),
    url(r'^user/resetPersonalInfo/$', User_views.resetPersonalInfo, name = 'resetPersonalInfo'),
    url(r'^user/getPersonalInfo/$', User_views.getPersonalInfo, name = 'getPersonalInfo'),
    url(r'^user/user/logout/$', User_views.logout, name = 'logout'),
    url(r'^admin/', admin.site.urls),
]
