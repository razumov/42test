from django import forms
from django.conf import settings


class Calendar(forms.DateInput):

    class Media:
        css = {
            'all': (
               'settings.MEDIA_URL + css/jquery-ui-1.8.13.custom.css',
            )}
        js = (
            'settings.MEDIA_URL + js/jquery-1.5.1.min.js',
            'settings.MEDIA_URL + js/jquery-ui-1.8.13.custom.min.js',
            'settings.MEDIA_URL + js/scripts.js',                  
        )