from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(obj):
    try:
        rendered_url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                obj._meta.module_name), args=(obj.pk,))
        return '<a href="%s">Edit object</a>' % rendered_url
    except:
        return "Not logged in"
