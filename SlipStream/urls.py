from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SlipStream.views.home', name='home'),
    # url(r'^SlipStream/', include('SlipStream.foo.urls')),

    url(r'^$', 'SlipStream.views.index'),
    url(r'^home/', 'show.views.home'),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^show/', include('show.urls')),

    url(r'^accounts/', include('registration.urls')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
