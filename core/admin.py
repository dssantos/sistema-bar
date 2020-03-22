from django.contrib import admin

from core.models import Categoria, Produto

class ProdutoModelAdmin(admin.ModelAdmin):
	list_display = ('nome_produto', 'preco', 'categoria')
	search_fields = ('nome_produto',)
	list_filter = ('categoria',)

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoModelAdmin)

admin.site.site_header = "Administração do Bar"
admin.site.site_title = "Administração do Bar"
admin.site.index_title = "Bar"