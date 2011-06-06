from django import forms
from models import Person
from widgets import Calendar


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        widgets = {'birth_date': Calendar}