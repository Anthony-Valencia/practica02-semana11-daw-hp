from django.db import models
class Producto(models.Model):
    CATEGORIAS=[('Laptops','Laptops'),('Smartphones','Smartphones'),('Audio','Audio'),('Gaming','Gaming'),('Accesorios','Accesorios'),('Wearables','Wearables')]
    nombre=models.CharField(max_length=120)
    precio=models.DecimalField(max_digits=9,decimal_places=2)
    categoria=models.CharField(max_length=30,choices=CATEGORIAS,db_index=True)
    stock=models.PositiveIntegerField(default=0)
    descripcion=models.TextField(blank=True)
    imagen_url=models.URLField(max_length=500,blank=True)
    etiqueta=models.CharField(max_length=32,blank=True)
    destacado=models.BooleanField(default=False)
    creado_en=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-creado_en']
        verbose_name_plural='Productos'
    def __str__(self):return self.nombre
