from .models import Produto, Categoria
from rest_framework import serializers

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Produto
		fields = '__all__'

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'