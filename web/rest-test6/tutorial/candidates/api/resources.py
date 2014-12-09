# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from restless.dj import DjangoResource

from candidates.models import Candidate
from core.api.dj import DjangoAngularResource
from core.api.helpers import from_data_to_instance
from core.restless.preparers import FieldsNullPreparer
from jobs.api.resources import AcademicBackgroundResource, LanguageBackgroundResource, ExperienceBackgroundResource, \
    DesiredProfessionResource, SkillBackgroundResource, VolunteeringBackgroundResource, HobbyBackgroundResource, \
    PortfolioBackgroundResource, ExperienceJobBackgroundResource, DrivingLicenseResource, \
    DrivingLicenseBackgroundResource


class CandidateResource(DjangoAngularResource):
    preparer = FieldsNullPreparer(fields={
        "id": "id",
        "freelance": "freelance",
        "user_id": "user.id",
        "nationality": "nationality",
        "country": "country",
        "state": "state",
        "city": "city",
        "address": "address",
        "postcode": "postcode",
        "gender": "gender",
        "extra_phone": "extra_phone",
        "disability_situation": "disability_situation.pk",
        "disability_grade": "disability_grade.pk",
        "disability_certification": "disability_certification",
        "objective": "objective",
        "own_vehicle": "own_vehicle",
        "minimum_salary_range": "minimum_salary_range.pk",
        "internship": "internship",
        "mobility": "mobility",
        "employment_status": "employment_status.pk",
        "availability": "availability.pk",
        "unemployment_card": "unemployment_card",
        "academic_backgrounds": "academic_backgrounds",
        "language_backgrounds": "language_backgrounds",
        "experience_backgrounds": "experience_backgrounds",
        "desired_professions": "desired_professions",
        "skill_backgrounds": "skill_backgrounds",
        "portfolio_backgrounds": "portfolio_backgrounds",
        "volunteering_backgrounds": "volunteering_backgrounds",
        "hobby_backgrounds": "hobby_backgrounds",
        "driving_licenses": "driving_licenses",
        "cover_letter": "cover_letter",
        "picture": "picture",
        "hidden": "hidden",
        "birth_date": "birth_date",
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated()

    @classmethod
    def urls(cls, name_prefix=None):
        return patterns(
            '',
            url(r'^$', cls.as_detail(), name=cls.build_url_name('detail', name_prefix)),
        )

    def detail(self):
        user = self.request.user
        return Candidate.objects.get(user=user)

    def update(self):
        """Create works as an update of the current candidate.
        :return:
        """
        user = self.request.user
        candidate = Candidate.objects.get(user=user)
        candidate = from_data_to_instance(Candidate, self.data, candidate)
        if self.data.get("hidden") is not None:
            candidate.hidden = bool(int(self.data.get("hidden")))
        candidate.save()
        return candidate

    @staticmethod
    def _prepare_m2m(field, resource_class):
        resource = resource_class()
        serialized_fields = list()
        for item in field.all():
            serialized_fields.append(resource.preparer.prepare(item))
        return serialized_fields

    @staticmethod
    def _prepare_experience_backgrounds(field):
        resource = ExperienceBackgroundResource()
        jobs_resource = ExperienceJobBackgroundResource()
        serialized_fields = list()
        for item in field.all():
            serialized_item = resource.preparer.prepare(item)
            serialized_item["jobs"] = list()
            for job in item.jobs.all():
                serialized_item["jobs"].append(jobs_resource.preparer.prepare(job))
            serialized_fields.append(serialized_item)
        return serialized_fields

    def prepare(self, data):
        prepped = super(CandidateResource, self).prepare(data)
        prepped['academic_backgrounds'] = self._prepare_m2m(prepped['academic_backgrounds'], AcademicBackgroundResource)
        prepped['language_backgrounds'] = self._prepare_m2m(prepped['language_backgrounds'], LanguageBackgroundResource)
        prepped['experience_backgrounds'] = self._prepare_experience_backgrounds(prepped['experience_backgrounds'])
        prepped['desired_professions'] = self._prepare_m2m(prepped['desired_professions'], DesiredProfessionResource)
        prepped['skill_backgrounds'] = self._prepare_m2m(prepped['skill_backgrounds'], SkillBackgroundResource)
        prepped['portfolio_backgrounds'] = self._prepare_m2m(prepped['portfolio_backgrounds'], PortfolioBackgroundResource)
        prepped['volunteering_backgrounds'] = self._prepare_m2m(prepped['volunteering_backgrounds'], VolunteeringBackgroundResource)
        prepped['hobby_backgrounds'] = self._prepare_m2m(prepped['hobby_backgrounds'], HobbyBackgroundResource)
        prepped['driving_licenses'] = self._prepare_m2m(prepped['driving_licenses'], DrivingLicenseBackgroundResource)
        prepped['cover_letter'] = {
            "url": prepped['cover_letter'].url if prepped['cover_letter'] else None
        }
        prepped['picture'] = {
            "type": "image",
            "urls": {
                "original": prepped['picture'].url if prepped['picture'] else None,
                "preview": prepped['picture'].get_thumbnail(
                    {'size': (109, 109), 'crop': 'smart', 'upscale': True, 'quality': 90}
                ).url if prepped['picture'] else None
            }
        }
        prepped['hidden'] = int(prepped['hidden'])
        prepped['internship'] = int(prepped['internship'])
        prepped['unemployment_card'] = int(prepped['unemployment_card'])
        prepped['disability_certification'] = int(prepped['disability_certification'])
        prepped['mobility'] = int(prepped['mobility'])
        prepped['own_vehicle'] = int(prepped['own_vehicle'])
        prepped['freelance'] = int(prepped['freelance'])

        return prepped