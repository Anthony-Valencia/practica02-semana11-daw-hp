from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[migrations.CreateModel(name='Producto',fields=[
       ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
       ('nombre',models.CharField(max_length=120)),('precio',models.DecimalField(decimal_places=2,max_digits=9)),
       ('categoria',models.CharField(choices=[('Laptops','Laptops'),('Smartphones','Smartphones'),('Audio','Audio'),('Gaming','Gaming'),('Accesorios','Accesorios'),('Wearables','Wearables')],db_index=True,max_length=30)),
       ('stock',models.PositiveIntegerField(default=0)),('descripcion',models.TextField(blank=True)),
       ('imagen_url',models.URLField(blank=True,max_length=500)),('etiqueta',models.CharField(blank=True,max_length=32)),
       ('destacado',models.BooleanField(default=False)),('creado_en',models.DateTimeField(auto_now_add=True))],
       options={'verbose_name_plural':'Productos','ordering':['-creado_en']})]
