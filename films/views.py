from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json

from django.template import RequestContext

from films.models import Series, Film, Link, Person

def home(request):
	return render_to_response('home.html',{
        }, context_instance=RequestContext(request))	

def list_series(request):
	return render_to_response('series/list.html',{
		'series':Series.objects.all(),
        }, context_instance=RequestContext(request))

def series(request, series_id):
	series = get_object_or_404(Series, id=series_id)
	films = Film.objects.filter(series=series).all()
	return render_to_response('series/view.html',{
		'series':series,
		'films':films,
        }, context_instance=RequestContext(request))

def list_people(request):
	return render_to_response('person/list.html',{
		'people':Person.objects.all(),
		}, context_instance=RequestContext(request))

def person(request, person_id):
	person = get_object_or_404(Person, id=person_id)
	return render_to_response('person/view.html',{
		'person':person,
		}, context_instance=RequestContext(request))


def film(request, film_id):
	film = get_object_or_404(Film, id=film_id)
	links = Link.objects.filter(film=film).all()
	return render_to_response('film/view.html',{
		'film':film,
		'links':links
        }, context_instance=RequestContext(request))
