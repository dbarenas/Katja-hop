from rest_framework import serializers
from .models import Libro, Author

class LibroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Libro
    fields = ('id', 'nombre', 'editorial', 'genero', 'author',)

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ('id', 'nombre', 'apellido',)
