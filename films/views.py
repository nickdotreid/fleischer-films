from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json

from django.template import RequestContext

def list_series(request):
	return render_to_response('base.html',{
        }, context_instance=RequestContext(request))

def view_series(request, series_id):
	return render_to_response('base.html',{
        }, context_instance=RequestContext(request))

def view_film(request, film_id):
	return render_to_response('base.html',{
        }, context_instance=RequestContext(request))
