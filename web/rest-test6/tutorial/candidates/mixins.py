# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from candidates.models import Candidate


class CandidateMixin(object):
    """Mixin to add candidate methods to AUTH_USER_MODEL."""

    def is_company(self):
        try:
            _ = self.candidate
        except (AttributeError, Candidate.DoesNotExist):
            return False
        return True