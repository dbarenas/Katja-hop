from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^snippets/code/(?P<pk>[0-9]+)$', views.snippet_attribute),
# 	url(r'^', include('candidates.urls', namespace='candidates')),
   	url(r'^api/candidate/?', include(CandidateResource.urls())),                                                                                                             

]

urlpatterns = format_suffix_patterns(urlpatterns)