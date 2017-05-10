from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^set_cords/$', views.set_cords),
	url(r'^get_cords/$', views.get_cords),
]