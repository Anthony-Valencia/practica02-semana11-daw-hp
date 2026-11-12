from django.core.management.base import BaseCommand
from catalogo.models import Producto

PRODUCTOS = [
('AeroBook Pro 16','Laptops',6799,8,'Laptop premium para productividad y diseño, pantalla inmersiva de 16 pulgadas.','photo-1496181133206-80ce9b88a853','TOP VENTAS',True),
('NovaBook Air 14','Laptops',3799,15,'Portátil ultraligera para estudiar, crear y trabajar desde cualquier lugar.','photo-1517336714731-489689fd1ca8','NUEVO',True),
('Titan Gaming RTX','Laptops',8999,4,'Potencia extrema, refrigeración avanzada y gráficos de alto rendimiento.','photo-1603302576837-37561b2e2302','EDICIÓN PRO',False),
('PixelMax Ultra','Smartphones',4299,12,'Smartphone insignia con sistema fotográfico avanzado y pantalla OLED.','photo-1511707171634-5f897ff02aa9','DESTACADO',True),
('NeoPhone Midnight','Smartphones',2899,22,'Diseño minimalista, cámara inteligente y batería de gran autonomía.','photo-1592750475338-74b7b21085ab','NUEVO',False),
('StudioSound ANC','Audio',899,28,'Audífonos over-ear inalámbricos con cancelación activa de ruido.','photo-1505740420928-5e560c06d30e','POPULAR',True),
('Pulse Buds Pro','Audio',549,33,'Audio inmersivo en un diseño compacto de larga duración.','photo-1606220588913-b3aacb4d2f46','',False),
('RGB Mechanical K75','Gaming',459,14,'Teclado mecánico de respuesta rápida, iluminación RGB personalizable.','photo-1541140532154-b024d705b90a','GAMING',False),
('Phantom Wireless Mouse','Gaming',329,26,'Mouse ergonómico, sensor de precisión y conectividad inalámbrica.','photo-1527814050087-3793815479db','',False),
('Vision 4K Display','Accesorios',1699,6,'Monitor de alta definición y colores vibrantes para entornos creativos.','photo-1527443224154-c4a3942d3acf','4K',False),
('Arc Smartwatch S','Wearables',749,0,'Reloj inteligente con seguimiento de actividad y diseño elegante.','photo-1523275335684-37898b6baf30','AGOTADO',False),
('DockStation USB-C','Accesorios',289,17,'Concentrador compacto para conectar todos tus dispositivos.','photo-1625842268584-8f3296236761','',False),
]
class Command(BaseCommand):
    help='Carga 12 productos de demostración; puede repetirse sin duplicarlos.'
    def handle(self,*args,**kwargs):
        for nombre,categoria,precio,stock,descripcion,foto,etiqueta,destacado in PRODUCTOS:
            Producto.objects.update_or_create(nombre=nombre,defaults=dict(categoria=categoria,precio=precio,stock=stock,descripcion=descripcion,imagen_url=f'https://images.unsplash.com/{foto}?auto=format&fit=crop&w=900&q=85',etiqueta=etiqueta,destacado=destacado))
        self.stdout.write(self.style.SUCCESS('12 productos cargados correctamente.'))
