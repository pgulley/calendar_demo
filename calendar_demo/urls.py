from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'calendar_demo.views.default', name='home'),
    url(r'^(\d{4})/(\d{2})/$', 'calendar_demo.views.index'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/$', 'calendar_demo.views.day'),
    # url(r'^calendar_demo/', include('calendar_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
