from django.conf.urls import url
from . import views


app_name = 'welcome'

urlpatterns = [
    url(r'^(\w+)/$', views.start, name='start'),
    url(r'^$', views.index, name='index'),
]
