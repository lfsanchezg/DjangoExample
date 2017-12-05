from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PetList.as_view(), name="url_list_pets"),
    url(r'^create/$', views.PetCreate.as_view(), name='create_pet_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.PetDetails.as_view(), name="detail_pet"),
    url(r'^delDuegno/$', views.owner_detail, name="duegno_detail"),
    url(r'^duegno/$', views.owner_list3)
]



