from django.db import models

class Categoria(models.Model):
	nome_categoria = models.CharField(max_length=200)

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"

	def __str__(self):
		return self.nome_categoria


class Produto(models.Model):
	nome_produto = models.CharField('Produto', max_length=200)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	preco = models.DecimalField('Preço (R$)', max_digits=5, decimal_places=2)

	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"

	def __str__(self):
		return self.nome_produto
