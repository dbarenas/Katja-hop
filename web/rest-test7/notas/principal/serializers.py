from rest_framework import serializers
from .models import Nota, Categoria


 
class NotaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nota
		field = ('titulo','description','categoria')
		depth = 1