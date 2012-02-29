from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^survey/$', 'survey.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^base/$', 'frontend.views.base'),
	url(r'^home/$', 'frontend.views.home'),
	url(r'^create survey/$', 'frontend.views.createsurvey'),
	url(r'^preview/$', 'frontend.views.preview'),
	url(r'^dashboard/$', 'frontend.views.dashboard'),
)
