from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Producto

def home(request):
    destacados=Producto.objects.filter(destacado=True,stock__gt=0).order_by('-creado_en')[:4]
    return render(request,'home.html',{'destacados':destacados,'total_productos':Producto.objects.count()})

class ProductoListView(ListView):
    model=Producto
    template_name='catalogo.html'
    context_object_name='productos'
    paginate_by=12
    def get_queryset(self):
        qs=Producto.objects.all()
        q=self.request.GET.get('q','').strip()[:100]
        categoria=self.request.GET.get('categoria','')
        disponibilidad=self.request.GET.get('disponibilidad','')
        orden=self.request.GET.get('orden','recientes')
        if q:qs=qs.filter(Q(nombre__icontains=q)|Q(descripcion__icontains=q)|Q(categoria__icontains=q))
        if categoria in dict(Producto.CATEGORIAS):qs=qs.filter(categoria=categoria)
        if disponibilidad=='stock':qs=qs.filter(stock__gt=0)
        campos={'precio_asc':'precio','precio_desc':'-precio','nombre':'nombre','recientes':'-creado_en'}
        return qs.order_by(campos.get(orden,'-creado_en'))
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categorias']=Producto.CATEGORIAS
        context['categoria_actual']=self.request.GET.get('categoria','')
        context['q']=self.request.GET.get('q','').strip()[:100]
        context['orden_actual']=self.request.GET.get('orden','recientes')
        context['disponibilidad_actual']=self.request.GET.get('disponibilidad','')
        context['total']=self.get_queryset().count()
        return context
