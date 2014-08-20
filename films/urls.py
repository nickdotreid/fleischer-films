from django.conf.urls import patterns, include, url

urlpatterns = patterns('films.views',
	url(r'^','list_series'),
)