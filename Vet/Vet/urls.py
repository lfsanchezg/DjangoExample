"""Vet URL Configuration

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
from Veterinaria.views import homeView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascotas/', include("Veterinaria.urls")),
    url(r'^$', homeView),
    #url(r'^', include('django.contrib.auth.urls')),
    url(r'^login/$', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
# URLS provistas por las url de autenticación:
# https://docs.djangoproject.com/en/1.11/topics/auth/default/#module-django.contrib.auth.views

#^logout/$ [name='logout']
#^password_change/$ [name='password_change']
#^password_change/done/$ [name='password_change_done']
#^login/$ [name='login']
#^password_reset/$ [name='password_reset']
#^password_reset/done/$ [name='password_reset_done']
#^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
#^reset/done/$ [name='password_reset_complete']