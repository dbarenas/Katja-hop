from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notas.views.home', name='home'),
    url(r'^', include('principal.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
