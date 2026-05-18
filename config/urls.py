from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [

    # Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # Users app
    path(
        '',
        include('users.urls')
    ),

    # Chat app
    path(
        'chat/',
        include('chat.urls')
    ),

]


# Media files
if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )