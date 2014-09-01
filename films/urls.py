from django.conf.urls import patterns, include, url

urlpatterns = patterns('films.views',
	url(r'^person/(?P<person_id>\w+)','person', name="person_view"),
	url(r'^person/','list_people', name="person_list"),
	url(r'^film/(?P<film_id>\w+)','film', name="film_view"),
	url(r'^series/(?P<series_id>\w+)','series', name="series_view"),
	url(r'^series/','list_series', name="series_list"),
	url(r'^','home'),
)