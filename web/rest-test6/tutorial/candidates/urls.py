# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from candidates.views import SignUpCandidateView, MyResume, SearchCandidatesView, ShowResumeView, ReceivedMessagesView, \
    SentMessagesView, ResumeToPDF


urlpatterns = patterns(
    '',
    url(r'^candidates/sign-up/$', SignUpCandidateView.as_view(), name="sign_up"),
    url(r'^candidates/my-resume/$', MyResume.as_view(), name="my_resume"),
    url(r'^candidates/my-resume/pdf/$', ResumeToPDF.as_view(), name="my_resume_pdf"),
    url(r'^candidates/search/$', SearchCandidatesView.as_view(), name="search"),
    url(r'^candidates/(?P<candidate_pk>\d+)/$', ShowResumeView.as_view(), name="show"),
    url(r'^candidates/(?P<candidate_pk>\d+)/pdf/$', ResumeToPDF.as_view(), name="show_pdf"),
    url(r'^candidates/messages/received/$', ReceivedMessagesView.as_view(), name="messages_received"),
    url(r'^candidates/messages/sent/$', SentMessagesView.as_view(), name="messages_sent"),
)

