from django.conf.urls import *

urlpatterns = patterns('show.views',
    url(r'^add$', 'add'),
    (r'^lookup/$', 'lookup'),
)