from rest_framework import serializers
from survey.models import Survey, SurveyVotes

class SurveySerializer(serializers.ModelSerializer):
  
  class Meta:
    
    model = Survey
    fields = ('title', 'question','owner', 'active')
