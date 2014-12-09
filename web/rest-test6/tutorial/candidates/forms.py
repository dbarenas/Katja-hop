# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from dateutil import relativedelta

from django import forms
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from candidates.models import Candidate
from companies.models import List
from core.choices import GENDER_CHOICES, BOOLEAN_CHOICES, BOOLEAN_NULL_CHOICES, GENDER_NULL_CHOICES
from jobs.models import Sector, Language, AcademicLevel, SectorSubcategory, Availability, City, State, Country, AgeRange
from profiles.forms import SignUpForm


class SignUpCandidateForm(SignUpForm):

    def save(self, commit=True):
        user = super(SignUpCandidateForm, self).save(commit=commit)
        if not commit:
            user.save()
        Candidate.objects.create(
            user=user,
        )
        return user


class SearchCandidatesForm(forms.Form):
    """Search for candidates."""

    sector = forms.ModelChoiceField(
        queryset=None,
        empty_label=_('Tipo de negocio'),
        required=False,
        label=_('Tipo de negocio'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subcategory = forms.CharField(
        required=False,
        label=_('Área'),
        widget=forms.HiddenInput(attrs={'class': 'form-control', "ng-value": "subcategory"})
    )
    position = forms.CharField(
        required=False,
        label=_('Puesto'),
        widget=forms.HiddenInput(attrs={'class': 'form-control', 'ng-value': "position"})
    )
    nationality = forms.CharField(
        required=False,
        label=_('Nacionalidad'),
        widget=forms.HiddenInput(attrs={'class': 'form-control', 'ng-value': "nationality"})
    )
    state = forms.CharField(
        required=False,
        label=_('Provincia'),
        widget=forms.HiddenInput(attrs={'class': 'form-control', 'ng-value': "state", "placeholder": _('Provincia')})
    )
    city = forms.CharField(
        required=False,
        label=_('Población'),
        widget=forms.HiddenInput(attrs={'class': 'form-control', 'ng-value': "city", "placeholder": _('Población')})
    )
    postcode = forms.CharField(
        required=False,
        label=_('C.P.'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _("C.P.")})
    )
    academic_level = forms.ModelChoiceField(
        queryset=None,
        empty_label=_('Nivel de estudios'),
        required=False,
        label=_('Nivel de estudios'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    academic_title = forms.CharField(
        required=False,
        label=_('Título'),
        widget=forms.HiddenInput(attrs={'class': 'form-control', "placeholder": _("Título"), "ng-value": "academic_title"})
    )
    center = forms.CharField(
        label=_('Centro'),
        required=False,
        widget=forms.HiddenInput(attrs={'class': 'form-control', "placeholder": _("Centro"), "ng-value": "center"})
    )
    languages = forms.ModelChoiceField(
        queryset=None,
        empty_label=_('Idiomas'),
        required=False,
        label=_('Idiomas'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    availability = forms.ModelChoiceField(
        queryset=None,
        empty_label=_('Disponibilidad'),
        required=False,
        label=_('Disponibilidad'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    age_range = forms.ModelChoiceField(
        queryset=None,
        empty_label=_('Edad'),
        required=False,
        label=_('Edad'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    gender = forms.CharField(
        label=_('Sexo'),
        required=False,
        widget=forms.Select(choices=GENDER_NULL_CHOICES, attrs={'class': 'form-control'})
    )
    my_lists = forms.ModelChoiceField(
        queryset=None,
        empty_label=_('Mis Listas'),
        label=_('Mis Listas'),
        required=False,
        widget=forms.Select(choices=BOOLEAN_NULL_CHOICES, attrs={'class': 'form-control'})
    )
    experience = forms.IntegerField(
        label=_('Experiencia'),
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    internship = forms.BooleanField(
        label=_('Prácticas'),
        required=False,
        widget=forms.Select(choices=BOOLEAN_NULL_CHOICES, attrs={'class': 'form-control'})
    )
    mobility = forms.BooleanField(
        label=_('Posib. desplazarse'),
        required=False,
        widget=forms.Select(choices=BOOLEAN_NULL_CHOICES, attrs={'class': 'form-control'})
    )
    disability_certification = forms.BooleanField(
        label=_('Cert. Discapacidad'),
        required=False,
        widget=forms.Select(choices=BOOLEAN_NULL_CHOICES, attrs={'class': 'form-control'})
    )
    unemployment_card = forms.BooleanField(
        label=_('Tarjeta deesempleo'),
        required=False,
        widget=forms.Select(choices=BOOLEAN_NULL_CHOICES, attrs={'class': 'form-control'})
    )
    freelance = forms.BooleanField(
        label=_('Autónomo'),
        required=False,
        widget=forms.Select(choices=BOOLEAN_NULL_CHOICES, attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user')
        if "user" in kwargs:
            del kwargs["user"]
        super(SearchCandidatesForm, self).__init__(*args, **kwargs)
        self.fields['sector'].queryset = Sector.objects.all()
        self.fields['academic_level'].queryset = AcademicLevel.objects.all()
        self.fields['languages'].queryset = Language.objects.all()
        self.fields['availability'].queryset = Availability.objects.all()
        self.fields['age_range'].queryset = AgeRange.objects.all()
        self.fields['my_lists'].queryset = List.objects.none()
        if self.user:
            self.fields['my_lists'].queryset = List.objects.filter(owner=self.user)

    @staticmethod
    def _queryset():
        return Candidate.objects.filter(hidden=False)

    def run(self, queryset=None):
        if queryset is None:
            queryset = self._queryset()
        # Sector filter
        sector = self.cleaned_data.get("sector")
        if sector:
            queryset = queryset.filter(
                Q(experience_backgrounds__sector=sector) |
                Q(desired_professions__sector=sector)
            )
        # Subcategory filter
        subcategory = self.cleaned_data.get("subcategory")
        if subcategory:
            queryset = queryset.filter(
                Q(experience_backgrounds__subcategory__icontains=subcategory) |
                Q(desired_professions__subcategory__icontains=subcategory)
            )
        # Academic level
        academic_level = self.cleaned_data.get("academic_level")
        if academic_level:
            queryset = queryset.filter(academic_backgrounds__level=academic_level)
        # Academic title
        academic_title = self.cleaned_data.get("academic_title")
        if academic_title:
            queryset = queryset.filter(academic_backgrounds__title=academic_title)
         # Academic center
        center = self.cleaned_data.get("center")
        if center:
            queryset = queryset.filter(academic_backgrounds__center=center)
        # Languages
        languages = self.cleaned_data.get("languages")
        if languages:
            queryset = queryset.filter(language_backgrounds__language=languages)
        # Lists
        my_lists = self.cleaned_data.get("my_lists")
        if my_lists:
            queryset = queryset.filter(lists__pk=my_lists.pk)
        # Age
        age_range = self.cleaned_data.get("age_range")
        if age_range:
            today = timezone.now().date()
            lower_date = today - relativedelta.relativedelta(years=age_range.lower)
            upper_date = today - relativedelta.relativedelta(years=age_range.upper)
            queryset = queryset.filter(birth_date__gte=upper_date).filter(birth_date__lte=lower_date)
        # Experience
        experience = self.cleaned_data.get("experience")
        if experience:
            queryset = queryset.filter(experience_backgrounds__years__gte=experience)
        # Position
        position = self.cleaned_data.get("position")
        if position:
            queryset = queryset.filter(experience_backgrounds__jobs__position__icontains=position)
        exact_fields = ["postcode", "availability", "gender",
                        "internship", "mobility", "disability_certification", "unemployment_card",
                        "freelance"]
        for field in exact_fields:
            value = self.cleaned_data.get(field)
            if value:
                queryset = queryset.filter(**{field: value})
        contains_fields = ["nationality", "state", "city"]
        for field in contains_fields:
            value = self.cleaned_data.get(field)
            if value:
                queryset = queryset.filter(**{"{}__icontains".format(field): value})
        return queryset.distinct()