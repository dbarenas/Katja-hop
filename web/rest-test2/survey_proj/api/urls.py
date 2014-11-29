from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views', 
    url(r'^surveys/$', 'survey_list', name='survey_list'),
    url(r'^survey/(?P[0-9]+)$', 'survey_details', name='survey_details'), 
)
