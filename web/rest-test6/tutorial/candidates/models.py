# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.helpers.files import UploadToDir


class Candidate():
    """User profile only for companies."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="candidate")
    nationality = models.CharField(max_length=255, verbose_name=_("nacionalidad"), null=True, blank=True)

    country = models.CharField(max_length=255, verbose_name=_("país"), null=True, blank=True)
    state = models.CharField(max_length=255, verbose_name=_("provincia"), null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name=_("población"), null=True, blank=True)
    address = models.CharField(verbose_name=_("dirección"), max_length=255, null=True, blank=True)

    postcode = models.CharField(verbose_name=_("código postal"), max_length=32, null=True, blank=True)
    gender = models.CharField(verbose_name=_("sexo"), max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    extra_phone = models.CharField(verbose_name=_("otro telefono"), max_length=32, null=True, blank=True)
    disability_situation = models.ForeignKey(
        "jobs.DisabilitySituation",
        verbose_name=_("situación de invalidez"), null=True, blank=True
    )
    disability_grade = models.ForeignKey(
        "jobs.DisabilityGrade",
        verbose_name=_("grado de discapacidad"), null=True, blank=True
    )
    disability_certification = models.BooleanField(
        verbose_name=_("posee certificado de discapacidad"), default=False
    )
    picture = ThumbnailerImageField(upload_to=UploadToDir("candidates"), null=True, blank=True)
    objective = models.TextField(verbose_name=_("objetivo"), null=True, blank=True)
    own_vehicle = models.BooleanField(
        verbose_name=_("vehículo propio"), default=False
    )
    minimum_salary_range = models.ForeignKey("jobs.SalaryRange", null=True, blank=True)
    hide_salary = models.BooleanField(
        verbose_name=_("esconder salario"), default=False
    )
    internship = models.BooleanField(
        verbose_name=_("posibilidad de ser contratado en prácticas"), default=False
    )
    mobility = models.BooleanField(
        verbose_name=_("posibilidad de desplazarse o cambiar de población"), default=False
    )
    employment_status = models.ForeignKey("jobs.EmploymentStatus", verbose_name=_("situación laboral"), null=True,
                                          blank=True)
    availability = models.ForeignKey("jobs.Availability", verbose_name=_("disponibilidad"), null=True, blank=True)
    unemployment_card = models.BooleanField(
        verbose_name=_("dispongo de tarjeta de desempleo"), default=False
    )
    freelance = models.BooleanField(
        verbose_name=_("eres autónomo"), default=False
    )
    driving_licenses = models.ManyToManyField("jobs.DrivingLicenseBackground", verbose_name=_("carné de conducción de vehículos"))
    academic_backgrounds = models.ManyToManyField("jobs.AcademicBackground")
    language_backgrounds = models.ManyToManyField("jobs.LanguageBackground")
    experience_backgrounds = models.ManyToManyField("jobs.ExperienceBackground")
    desired_professions = models.ManyToManyField("jobs.DesiredProfession")
    skill_backgrounds = models.ManyToManyField("jobs.SkillBackground")
    portfolio_backgrounds = models.ManyToManyField("jobs.PortfolioBackground")
    volunteering_backgrounds = models.ManyToManyField("jobs.VolunteeringBackground")
    hobby_backgrounds = models.ManyToManyField("jobs.HobbyBackground")
    cover_letter = models.FileField(upload_to=UploadToDir("covers"), null=True, blank=True)

    birth_date = models.DateField(verbose_name=_("fecha de nacimiento"), null=True, blank=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Candidato")
        verbose_name_plural = _("Candidatos")

    def get_picture(self, size=(137, 124)):
        url = "http://placehold.it/{}x{}".format(size[0], size[1])
        if self.picture:
            url = self.picture.get_thumbnail(
                {'size': size, 'crop': 'smart', 'upscale': True, 'quality': 90}
            ).url
        return url