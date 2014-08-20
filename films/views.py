from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json

from django.template import RequestContext

from films.models import Series, Film

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

def film(request, film_id):
	return render_to_response('base.html',{
        }, context_instance=RequestContext(request))
