from django.db import models


class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	indentifier = models.IntegerField(default=0)
	GPS_coordinates = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	site_category = models.CharField(max_length=100)
	area = models.CharField(max_length=100)
	deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombre

# Create your models here.
class Nota(models.Model):
	titulo = models.CharField(max_length=200)
	description = models.TextField()

	category = models.ForeignKey(Categoria)

	#track = models.ForeignKey(SetSiteTracks)
	track = models.IntegerField(default=0)
	producer = models.CharField(max_length=100)
	#category = models.CharField(max_length=100)
	rating = models.IntegerField(default=0)
	classification = models.CharField(max_length=100)
	atype = models.CharField(max_length=100)
	date_recorded = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	artist = models.CharField(max_length=100) 
	language = models.CharField(max_length=100)
	identifier = models.CharField(max_length=10)
	background_image = models.CharField(max_length=100)  
	deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.titulo