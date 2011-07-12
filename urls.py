from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import django.views.static
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test42.views.home', name='home'),
     url(r'^', include('app.urls')),
     
     (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__),
                                       "media/css").replace('\\', '/')}),
                       
     (r'^js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__),
                                       "media/js").replace('\\', '/')}),

     (r'^images/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__),
                                       "media/images").replace('\\', '/')})
)
                       
if settings.DEBUG:                       
    urlpatterns += patterns('',
         (r'^media/(?P<path>.*)$', django.views.static.serve, 
             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
                                
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

