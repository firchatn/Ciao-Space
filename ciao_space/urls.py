from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^' + settings.ADMIN_PATH + '/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^space/', include('space.urls')),
    url(r'^', include('welcome.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG and settings.DEBUG_TOOLBAR_INSTALLED:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
