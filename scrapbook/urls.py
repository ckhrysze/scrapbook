from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/(.*)', admin.site.root),

    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_DOC_ROOT}),
    (r'^static/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.STATIC_DOC_ROOT}),


    (r'^', include('scrapbook.sbmain.urls')),
)
