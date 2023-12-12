from django.contrib import admin
from .models import Cliente, Pedido, Producto

class PedidoAdmin(admin.ModelAdmin):
    exclude = ('numero',)


admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)