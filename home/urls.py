from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'home'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^Detail_view/(?P<pk>[0-9]+)/$', views.DetailView, name='Post_view'),
	url(r'^Ubermensch', views.Ubermensch),
	url(r'^Pensamientos', views.Pensamientos),
	url(r'^Historias', views.Historias),
	url(r'^Ciencia', views.Ciencia),
	url(r'^search', views.Search),
	url(r'^contacto', views.Search, name='contacto'),
	url(r'^acerca', views.Search, name='acerca'	),
	url(r'^Post_comment/(?P<pk>[0-9]+)$', views.Post_comment, name='Post_comment'),
	url(r'^Post_scomment/(?P<pk>[0-9]+)$', views.Post_scomment, name='Post_scomment'),
]
