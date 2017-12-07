from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PetList.as_view(), name="url_list_pets"),
    url(r'^create/$', views.PetCreate.as_view(), name='create_pet_view'),
    url(r'^createPersonalized/$', views.create_pet, name='create_pet_view2'),
    url(r'^(?P<pk>[0-9]+)/$', views.PetDetails.as_view(), name="detail_pet"),
    url(r'^duegno/(?P<duegno_id>[0-9]+)/$', views.owner_detail, name="duegno_detail"),
    url(r'^createDuegno/$', views.DuegnoCreate.as_view(), name="create_duegno"),
    url(r'^duegno/$', views.duegno_list, name='duegno_list_view')
]



