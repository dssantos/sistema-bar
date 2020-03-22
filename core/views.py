from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer


def index(request):
     return HttpResponse("Bar")

class ProdutoViewSet(viewsets.ModelViewSet):

	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer
	permission_classes = [permissions.IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):

	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer
	permission_classes = [permissions.IsAuthenticated]