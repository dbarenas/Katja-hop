# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from braces.views import LoginRequiredMixin

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.views.generic import View
from wkhtmltopdf.views import PDFTemplateView

from candidates.forms import SignUpCandidateForm, SearchCandidatesForm
from candidates.models import Candidate
from core.helpers import calculate_age
from core.wkhtmltopdf.views import CustomPDFTemplateResponse
from jobs.models import Message


class SignUpCandidateView(View):

    @staticmethod
    def get(request):
        data = {
            "form": SignUpCandidateForm()
        }
        return render(request, "candidates/sign_up.html", data)

    @staticmethod
    def post(request):
        form = SignUpCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                email=request.POST['email'],
                password=request.POST['password']
            )
            login(request, user)
            return redirect("candidates:my_resume")
        data = {
            "form": form
        }
        return render(request, "candidates/sign_up.html", data)


class MyResume(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "candidates/resumes/form.html")


class SearchCandidatesView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        form = SearchCandidatesForm(request.GET, user=request.user)
        candidates = Candidate.objects.none()
        if form.is_valid() and len(request.GET):
            candidates = form.run()
        candidates.select_related("user")
        data = {
            "form": form,
            "candidates": candidates,
            "is_query": len(request.GET) > 0,
        }
        return render(request, "candidates/search.html", data)


class ShowResumeView(LoginRequiredMixin, View):

    @staticmethod
    def get(request, candidate_pk):
        candidate = get_object_or_404(Candidate, pk=candidate_pk)
        form = SearchCandidatesForm(user=request.user)
        data = {
            "candidate": candidate,
            "candidate_picture": candidate.get_picture(),
            "candidate_age": calculate_age(candidate.birth_date),
            "academic_backgrounds": candidate.academic_backgrounds.all(),
            "language_backgrounds": candidate.language_backgrounds.all(),
            "experience_backgrounds": candidate.experience_backgrounds.all(),
            "desired_professions": candidate.desired_professions.all(),
            "skill_backgrounds": candidate.skill_backgrounds.all(),
            "portfolio_backgrounds": candidate.portfolio_backgrounds.all(),
            "volunteering_backgrounds": candidate.volunteering_backgrounds.all(),
            "driving_licenses": candidate.driving_licenses.all(),
            "hobby_backgrounds": candidate.hobby_backgrounds.all(),
            "form": form,
        }
        return render(request, "candidates/show.html", data)


class ReceivedMessagesView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        Message.objects.filter(destination=request.user).update(read=True)
        messages = Message.objects.filter(destination=request.user)
        data = {
            "messages": messages
        }
        return render(request, "candidates/messages/received.html", data)


class SentMessagesView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        messages = Message.objects.filter(origin=request.user)
        data = {
            "messages": messages
        }
        return render(request, "candidates/messages/sent.html", data)


class ResumeToPDF(LoginRequiredMixin, PDFTemplateView):
    filename = 'cv.pdf'
    template_name = 'candidates/resumes/pdf.html'
    cmd_options = {
        "margin-bottom": 0,
        "margin-left": 0,
        "margin-right": 0,
        "margin-top": 0,
    }
    response_class = CustomPDFTemplateResponse

    def get(self, request, *args, **kwargs):
        self.candidate = None
        if "candidate_pk" in kwargs:
            try:
                self.candidate = Candidate.objects.get(pk=kwargs.get("candidate_pk"))
            except Candidate.DoesNotExist:
                pass
        return super(ResumeToPDF, self).get(request, *args, **kwargs)

    def get_filename(self):
        candidate = self.candidate
        if candidate is None:
            candidate = self.request.user.candidate
        return "cv-{}.pdf".format(slugify(candidate.user.get_full_name()))

    def render_to_response(self, context, **response_kwargs):
        if not context:
            context = {}
        if self.candidate is None:
            context["candidate"] = self.request.user.candidate
            context["candidate_picture"] = self.request.user.candidate.get_picture((100, 130))
        else:
            context["candidate"] = self.candidate
            context["candidate_picture"] = self.candidate.get_picture((100, 130))
        return super(ResumeToPDF, self).render_to_response(context, **response_kwargs)