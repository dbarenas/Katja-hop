# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from core.helpers import calculate_age


register = template.Library()


@register.inclusion_tag('candidates/templatetags/list_entry_candidate.html', takes_context=True)
def list_candidate(context, candidate, is_search_result=False, offer=None, company=None):
    context["candidate"] = candidate
    context["candidate_age"] = calculate_age(candidate.birth_date)
    context["candidate_picture"] = candidate.get_picture()
    context["is_search_result"] = is_search_result
    context["offer"] = offer
    context["company"] = company
    return context


@register.inclusion_tag('candidates/templatetags/grid_entry_candidate.html', takes_context=True)
def grid_candidate(context, candidate):
    context["candidate"] = candidate
    context["candidate_age"] = calculate_age(candidate.birth_date)
    context["candidate_picture"] = candidate.get_picture((109, 109))
    return context