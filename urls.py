from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = \
patterns('',
         url(r'^$', 'dashboard.views.home', name='home'),
         url(r'^calendar/', 'dashboard.views.calendar', name='calendar'),
         url(r'^events/', 'dashboard.views.events', name='events'),
         url(r'^nextbus/', 'dashboard.nextbus.nextbus', name='nextbus'),
         url(r'^weather/', 'dashboard.views.weather', name='weather'),
         url(r'^news/', 'dashboard.views.news', name='news'),
         url(r'^localnews/', 'dashboard.views.localnews', name='news'),
         url(r'^light', 'dashboard.views.light', name='light'),
         
    # url(r'^dashboard/', include('dashboard.foo.urls')),
         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT,
             }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.STATIC_ROOT,
             }),   

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
