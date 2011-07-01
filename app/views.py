from django.shortcuts import render_to_response
from models import Person, Request
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from forms import PersonForm
import receiver
import tools


def person_views(request):
    c = tools.get_default_context(request, 'm_person')
    c['p'] = Person.objects.all()[0]
    return render_to_response('person.html', c, \
                              context_instance=RequestContext(request))


def request_view(request):
    if request.is_ajax():
        id = request.POST.get("id", 0)
        if id:
            req = Request.objects.get(id=int(id))
            req.priority += 1
            req.save()
            return HttpResponse(id + ";" + str(req.priority))
    c = tools.get_default_context(request, 'm_requests')
    if int(request.POST.get('priority', 0)):
        c['high'] = True
        c['requests'] = Request.objects.order_by('-priority','-date')[:10]
    else:
        c['requests'] = Request.objects.order_by('priority','-date')[:10]
    return render_to_response('requests.html', c, \
                              context_instance=RequestContext(request))
    
    
@login_required
def edit_view(request):
    c = tools.get_default_context(request, 'm_edit')
    if request.method == 'POST': 
        form = PersonForm(request.POST, instance=Person.objects.all()[0])
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse("Saved!")
            return HttpResponseRedirect('/')
    else:
        p = Person.objects.all()[0]
        form = PersonForm(instance=p) 

    c['form'] = form
    return render_to_response('edit.html', c,
                              context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return person_views(request)


def tag_view(request):
    c = tools.get_default_context(request, 'm_tag')
    return render_to_response('tag.html', c,
                               context_instance=RequestContext(request))