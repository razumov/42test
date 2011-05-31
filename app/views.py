from django.shortcuts import render_to_response
from models import Person, Request
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from forms import PersonForm
import tools


def person_views(request):
    c = tools.get_default_context(request, 'm_person')
    c['p'] = Person.objects.all()[0]
    return render_to_response('person.html', c, \
                              context_instance=RequestContext(request))


def request_view(request):
    c = tools.get_default_context(request, 'm_requests')
    try:
        c['requests'] = Request.objects.order_by('-date')[:10]
    except:
        pass
    return render_to_response('requests.html', c, \
                              context_instance=RequestContext(request))
    
    
@login_required
def edit_view(request):
    c = tools.get_default_context(request, 'm_edit')
    if request.method == 'POST': 
        form = PersonForm(request.POST) 
        if form.is_valid(): 
            p = Person.objects.all()[0]
            p.name = form.cleaned_data['name']
            p.surname = form.cleaned_data['surname']
            p.bio = form.cleaned_data['bio']
            p.contacts = form.cleaned_data['contacts']
            p.save()
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
