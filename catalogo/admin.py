from django.contrib import admin
from .models import Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','categoria','precio','stock','destacado')
    list_filter=('categoria','destacado')
    search_fields=('nombre','descripcion')
    list_editable=('precio','stock','destacado')
