# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from candidates.models import Candidate
from jobs.admin import LanguageBackgroundInline, AcademicBackgroundInline, ExperienceBackgroundInline, \
    DesiredProfessionInline, PortfolioBackgroundInline, VolunteeringBackgroundInline, HobbyBackgroundInline


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'country', 'state', 'city', 'created')
    inlines = [
        AcademicBackgroundInline,
        LanguageBackgroundInline,
        ExperienceBackgroundInline,
        DesiredProfessionInline,
        PortfolioBackgroundInline,
        VolunteeringBackgroundInline,
        HobbyBackgroundInline,
    ]
    exclude = (
        "language_backgrounds", "desired_professions", "experience_backgrounds", "academic_backgrounds",
        "skill_backgrounds", "portfolio_backgrounds", "volunteering_backgrounds", "hobby_backgrounds",
    )

admin.site.register(Candidate, CandidateAdmin)

