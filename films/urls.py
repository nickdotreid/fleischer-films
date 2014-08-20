from django.conf.urls import patterns, include, url

urlpatterns = patterns('films.views',
	url(r'^film/(?P<film_id>\w+)','film', name="film_view"),
	url(r'^series/(?P<series_id>\w+)','series'),
	url(r'^','list_series'),
)