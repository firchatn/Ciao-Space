from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^(\w+)/$', views.start, name='start'),
        url(r'^$', views.startapp, name='startapp'),
	]