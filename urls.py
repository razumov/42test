from django.conf.urls.defaults import patterns, include
from django.conf import settings


urlpatterns = patterns('',

            (r'', include('app.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',

        (r'^%s/css/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
         'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT + '/css'}),

        (r'^%s/js/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
         'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT + '/js'}),

        (r'^%s/images/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
         'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT + '/images'}),
)
