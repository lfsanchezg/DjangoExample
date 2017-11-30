from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListView.as_view(), name="url_list_pets"),
    url(r'^create/$', views.CreateView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PetDetails.as_view()),
]
