from django.contrib import admin

from gestion_pedidos.models import Clientes, Articulos, Pedidos



# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'telefono', 'email')
    search_fields=('id', 'nombre', 'direccion', 'telefono', 'email')
    list_filter=("nombre",)

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')
    search_fields=('nombre', 'seccion', 'precio')
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')
    search_fields=('numero', 'fecha', 'entregado')
    list_filter=("fecha","entregado",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)
