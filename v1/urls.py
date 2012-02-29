from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^index/$', 'frontend.views.index'),
	url(r'^home/$', 'frontend.views.home'),
)
