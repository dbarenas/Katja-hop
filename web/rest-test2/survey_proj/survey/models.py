from django.db import models


class Survey(models.Model):
  owner = models.CharField(max_length=100)
  title = models.CharField(max_length=50)
  question = models.CharField(max_length=300)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated = models.DateTimeField(auto_now_add=False,auto_now=True)
# Create your models here.

class SurveyVotes(models.Model):
  ownerv = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated = models.DateTimeField(auto_now_add=False,auto_now=True)