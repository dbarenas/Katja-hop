from rest_framework import viewsets
from .models import Nota, Categoria
from .serializers import NotaSerializer

 

class NotaViewSet(viewsets.ModelViewSet):
	queryset = Nota.objects.all()
	serializer_class = NotaSerializer