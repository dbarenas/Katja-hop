from django.shortcuts import render

# Create your views here. from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from survey.models import Survey 
from .serializers import SurveySerializer
@api_view(['GET', 'POST']) 
def survey_list(request):
	'''
	List all surveys, or create a new survey
	'''
	if request.method == 'GET':
		survey = Survey.objects.all() 
		serializer = SurveySerializer(survey) 
		return Response(serializer.data) 
	elif request.method == 'POST': 
		serializer = SurveySerializer(data=request.DATA) 
		if serializer.is_valid(): 
			serializer.save() 
			return Response(serializer.data, status=status.HTTP_201_CREATED) 
	else: 
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT', 'DELETE']) 
def survey_details(request, pk): 
	'''
	Get, update, or delete a specific survey 
	'''
	try: 
		survey = Survey.objects.get(pk=pk) 
	except Survey.DoesNotExist: 
		return Response(status=status.HTTP_404_NOT_FOUND) 
	if request.method == 'GET': 
		serializer = SurveySerializer(survey) 
		return Response(serializer.data) 
	if request.method == 'PUT': 
		serializer = SurveySerializer(survey, data=request.DATA) 
		if serializer.is_valid(): 
			serializer.save() 
			return Response(serializer.data) 
		else: 
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		survey.delete() 
		return Response(status=status.HTTP_204_NO_CONTENT)