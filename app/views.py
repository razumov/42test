from django.shortcuts import render_to_response
from models import Person, Request
<<<<<<< HEAD
from django.template import RequestContext
=======
>>>>>>> t3_middleware


def person_views(request):
    p = Person.objects.all()[0]
<<<<<<< HEAD
    return render_to_response('person.html', {'p': p}, \
                              context_instance=RequestContext(request))
=======
    return render_to_response('person.html', {'p': p})
>>>>>>> t3_middleware


def request_view(request):
    try:
<<<<<<< HEAD
        requests = Request.objects.all()[:10]
    except:
        requests = None
    return render_to_response('requests.html', {'requests': requests}, \
                              context_instance=RequestContext(request))
=======
        requests = Request.objects.order_by('-date')[:10]
    except:
        requests = None
    return render_to_response('requests.html', {'requests': requests})
>>>>>>> t3_middleware
