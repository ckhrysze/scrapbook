from django.conf.urls.defaults import *

urlpatterns = patterns('scrapbook.sbmain.views',

    (r'^landing', 'landing'),
    (r'^blog', 'blog'),

    (r'^galleries', 'galleries'),
    (r'^gallery/(\d+)/$', 'gallery'),

    (r'^portraits/(\d+)/$', 'portraits'),
    (r'^portraits', 'portraits_list'),

    (r'^login', 'sblogin'),
    (r'^logout', 'sblogout'),

    (r'^videos', 'videos'),

    (r'^index$', 'index'),
    (r'^$', 'index'),
)
