from django import forms
from models import Person
from widgets import Calendar


class PersonForm(forms.ModelForm):
    
    def __init__(self, *args, **kw):
        super(forms.ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()

    class Meta:
        model = Person
        widgets = {'birth_date': Calendar}