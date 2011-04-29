from django.shortcuts import render_to_response
from models import Person





def person_views (request):
    p = Person.objects.all()[0]
    return render_to_response ('person.html', {'p' : p})
    

	

