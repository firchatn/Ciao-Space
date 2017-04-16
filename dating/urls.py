
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^startapp/', include('welcome.urls')),
    url(r'^singup/', include('singup.urls')),
    url(r'^space/', include('space.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)