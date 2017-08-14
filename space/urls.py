from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(\w+)/$', views.contrainer, name='contrainer'),
    url(r'^post/$', views.new_post, name='new_post'),
    url(r'^(\w+)/(\w+)/post/$', views.new_post, name='new_post'),
    url(r'^(\w+)/(\w+)/$', views.profil, name='profil'),
    url(r'^(\w+)/(\w+)/message/$', views.message, name='message'),
]
