from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^notepost$', views.postnote),
    url(r'^editnote/(?P<id>\d+)$', views.editnote),
    url(r'^deletenote/(?P<id>\d+)$', views.deletenote),
    url(r'^notes$', views.allnotes)
]