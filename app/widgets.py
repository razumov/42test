from django import forms


class Calendar(forms.DateInput):

    class Media:
        css = {
            'all': (
                "css/jquery-ui-1.8.13.custom.css",
            )}
        js = (
            '/js/jquery-1.5.1.min.js',
            "/js/jquery-ui-1.8.13.custom.min.js",
            "/js/scripts.js"                  
        )