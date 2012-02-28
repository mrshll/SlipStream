from django.conf.urls import *

urlpatterns = patterns('show.views',
    url(r'^add$', 'add'),
    (r'^lookup/$', 'lookup'),
    (r'^(?P<show_id>\d+)','get')
)