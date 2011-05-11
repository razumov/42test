from django.shortcuts import render_to_response
from models import Person, Request
from django.template import RequestContext


def person_views(request):
    p = Person.objects.all()[0]
    return render_to_response('person.html', {'p': p}, context_instance=RequestContext(request))


def request_view(request):
    try:
        requests = Request.objects.all()[:10]
    except:
        requests = None
    return render_to_response('requests.html', {'requests': requests}, context_instance=RequestContext(request))
