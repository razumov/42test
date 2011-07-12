from django.conf.urls.defaults import *
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', views.person_views, name="person"),
      url(r'^requests/$', views.request_view, name="requests"),
      url(r'^logout/$', views.logout_view, name="logout"),
      url(r'^edit/$', views.edit_view, name="edit"),
      url(r'^tag/$', views.tag_view, name="tag"),

      (r'^admin/doc/', include('django.contrib.admindocs.urls')),

      (r'^admin/', include(admin.site.urls)),
      (r'^accounts/login/$', 'django.contrib.auth.views.login',
                                  {'template_name': 'login.html'})
                       

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
