from .models import Libro, Author
from .serializers import LibroSerializer, AuthorSerializer
from rest_framework import viewsets
 
class LibroViewSet(viewsets.ModelViewSet):
  serializer_class = LibroSerializer
  queryset = Libro.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
  serializer_class = AuthorSerializer
  queryset = Author.objects.all()
                        
