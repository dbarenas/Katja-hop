from django.db import models

class Author(models.Model):
  
  nombre = models.TextField(max_length=100)
  apellido = models.TextField(max_length=100)

class Libro(models.Model):

  nombre = models.TextField(max_length=100)
  editorial = models.TextField(max_length=100)
  genero = models.TextField(max_length=100)
  author = models.ForeignKey(Author)
# Create your models here.
